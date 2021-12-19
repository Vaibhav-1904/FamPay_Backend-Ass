from django.shortcuts import render
import requests
from django.http import JsonResponse
from .models import video
import json


def show_latest_videos(request):
    # collecting the response from the Youtube API
    # search query = official
    response = requests.get('https://youtube.googleapis.com/youtube/v3/search?part=snippet&order=date&q=official&key=AIzaSyDCa32_gehikY8wO2EOm3kYStQE27aGXhA')
    
    if response.status_code == 200:
        response = response.json()["items"]
        # return JsonResponse(response, safe=False)

        # Storing Video Details in the Database(video Model)
        for v in response:
            try:
                title = v.snippet.title
                desc = v.snippet.description
                dt = v.snippet.publishedAt
                url = v.snippet.thumbnails.medium.url
                channel = v.snippet.channelTitle

                obj = video(channel_title = channel, video_title = title, video_description = desc, date_time = dt, thumbnail_url = url)
                obj.save()
            except:
                continue

        # return index page with response to show videos in chronological order with paginated response
        return render(request, 'main/index.html', {'response': response})
    else:
        return render(request, 'main/index.html', {'response': response})
    


# def start(request):
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(show_latest_videos, 'interval', seconds=10)
#     scheduler.start()