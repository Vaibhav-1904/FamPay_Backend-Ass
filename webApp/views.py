from django.shortcuts import render
import requests
from django.http import JsonResponse
from .models import video
import json


def show_latest_videos(request):
    # collecting the response from the Youtube API
    # search query = official

    search_url = 'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=15&order=date&q=official&key=AIzaSyAR8YCmbh_qMwI6-Ke1INSgLeYWUs2oUt0'
    response = requests.get(search_url) # Collecting the response from the Youtube API
    
    if response.status_code == 200:
        response = response.json()["items"] # response contains the search query result in a JSON Object

        # Storing Video Details in the Database(video Model)
        n = len(response)
        for i in range(n):
            try:
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
            except:
                continue


        # if you want to run the API in PostMan, uncomment the line belowJsonResponse(response, safe=False) Hand
        # comment down the lines after the below line, since PostMan requires a JSON Object. 
        
        # return JsonResponse(response, safe=False)


        # return index page with response to show videos in chronological order with paginated response
        return render(request, 'main/index.html', {'response': response})
    else:
        return render(request, 'main/index.html', {'response': response})
    
