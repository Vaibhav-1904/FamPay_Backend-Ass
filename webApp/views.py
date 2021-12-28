from django.shortcuts import render
import json, asyncio, aiohttp
from asgiref.sync import sync_to_async
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import videoSerializer
from .models import video


class VideoView(APIView): # API used for displaying stored video data in a paginated response 
                            # sorted in descending order of published datetime.

    def get(self, request):

        fetch_latest_videos(request)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        task = loop.create_task(fetch_latest_videos(request))
        loop.run_until_complete(task)

        # converting queryset data into JSON using serializer
        queryset = video.objects.all().order_by('-date_time') 
        serializer = videoSerializer(queryset, many = True) 
        return Response(serializer.data)
        

async def fetch(client, url):
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.json()

# search query = official
async def fetch_latest_videos(request):

    # collecting the response from the Youtube API with asyncio
    search_url = ['https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=15&order=date&q=official&key=AIzaSyAR8YCmbh_qMwI6-Ke1INSgLeYWUs2oUt0']
    async with aiohttp.ClientSession() as client:
        tasks = []
        task = asyncio.ensure_future(fetch(client, search_url[0]))
        tasks.append(task)

        qs = await asyncio.gather(*tasks) # qs contains the search query result in a JSON Object

    
    response = qs[0]["items"] # fetching item from JSON object

    await Store_Videos_DB(response) # storing video details in database


# Below Function is used to store to videos obtained from Youtube API to our database
@sync_to_async
def Store_Videos_DB(response):

    # Storing Video Details in the Database(video Model)

    if len(video.objects.all()) != 0:
        index = len(video.objects.all())
    else:
        index = 0

    n = len(response)
    for i in range(n):
        index = index + 1
        title = response[i]["snippet"]["title"]
        desc = response[i]["snippet"]["description"]
        dt = response[i]["snippet"]["publishedAt"]
        url = response[i]["snippet"]["thumbnails"]["medium"]["url"]
        channel = response[i]["snippet"]["channelTitle"]

        obj = video(
            index = index,
            channel_title = channel, 
            video_title = title, 
            video_description = desc, 
            date_time = dt, 
            thumbnail_url = url)
        obj.save()
    


# Dashboard API with Sorting option for stored videos
class DashboardView(APIView):

    def get(self, request):
        # creating a query for sorting videos
        sort_type = self.request.query_params.get('sort')

        if sort_type != None:
            if sort_type == 'video_title':
                all_videos = video.objects.all().order_by('video_title')
            elif sort_type == 'channel_title':
                all_videos = video.objects.all().order_by('channel_title')
        else:
            all_videos = video.objects.all()

        # serializer = videoSerializer(all_videos, many = True)
        # return Response(serializer.data) 
        return render(request, 'main/dashboard.html', {'all_videos': all_videos})
