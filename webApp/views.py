from django.shortcuts import render
import requests
from django.http import JsonResponse
from .models import video
import json


def show_latest_videos(request):
    # collecting the response from the Youtube API
    # search query = official
    response = requests.get('https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=15&order=date&q=official&key=AIzaSyAR8YCmbh_qMwI6-Ke1INSgLeYWUs2oUt0')
    
    if response.status_code == 200:
        response = response.json()["items"] # response contains the search query result in a JSON Object
        
        # if you want to run the API in PostMan, uncomment the line belowJsonResponse(response, safe=False) Hand
        # comment down the lines after the below line, since PostMan requires a JSON Object. 
        
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