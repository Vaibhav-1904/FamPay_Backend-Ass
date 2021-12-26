from django.shortcuts import render
import requests
from django.http import JsonResponse
import json, asyncio, aiohttp
from asgiref.sync import sync_to_async
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import videoSerializer
from .models import video


class VideoView(APIView): # Function used for displaying stored video data in a paginated response 
                            # sorted in descending order of published datetime.

    def get(self, request):

        show_latest_videos(request)

        # converting queryset data into JSON
        queryset = video.objects.all() 
        serializer = videoSerializer(queryset, many = True) 
        return Response(serializer.data)
        

async def fetch(client, url):
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.json()

# search query = official
async def show_latest_videos(request):

    # collecting the response from the Youtube API with asyncio
    search_url = ['https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=15&order=date&q=official&key=AIzaSyAR8YCmbh_qMwI6-Ke1INSgLeYWUs2oUt0']
    async with aiohttp.ClientSession() as client:
        tasks = []
        task = asyncio.ensure_future(fetch(client, search_url[0]))
        tasks.append(task)

        qs = await asyncio.gather(*tasks) # qs contains the search query result in a JSON Object

    
    response = qs[0]["items"] # fetching item from JSON object

    await store_videos_db(response) # storing video details in database


# Below Function is used to store to videos obtained from Youtube API to our database
@sync_to_async
def store_videos_db(response):
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
    


def show_dashboard(request):

    all_videos = video.objects.all()

    return render(request, 'main/dashboard.html', {'all_videos': all_videos})