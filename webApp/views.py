from django.shortcuts import render
import requests
from django.http import JsonResponse
from .models import video
import json, asyncio, aiohttp
from asgiref.sync import sync_to_async


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
        for url in search_url:
            task = asyncio.ensure_future(fetch(client, url))
            tasks.append(task)

        qs = await asyncio.gather(*tasks)

    
    response = qs[0]["items"] # response contains the search query result in a JSON Object

    store_videos_db(response)

    # if you want to run the API in PostMan, uncomment the line belowJsonResponse(response, safe=False) Hand
    # comment down the lines after the below line, since PostMan requires a JSON Object. 
        
    # return JsonResponse(response, safe=False)

    # return index page with response to show videos in chronological order with paginated response
    return render(request, 'main/index.html', {'response': response})

@sync_to_async
def store_videos_db(response):
    # Storing Video Details in the Database(video Model)
    n = len(response)
    for i in range(n):
        title = response[i]["snippet"]["title"]
        desc = response[i]["snippet"]["description"]
        dt = response[i]["snippet"]["publishedAt"]
        url = response[i]["snippet"]["thumbnails"]["medium"]["url"]
        channel = response[i]["snippet"]["channelTitle"]

        obj = video(
            channel_title = channel, 
            video_title = title, 
            video_description = desc, 
            date_time = dt, 
            thumbnail_url = url)
        obj.save()
    