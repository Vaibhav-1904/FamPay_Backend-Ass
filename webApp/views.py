from django.shortcuts import render
import requests
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
import json
from apscheduler.schedulers.background import BackgroundScheduler

def show_latest_videos(request):
    response = requests.get('https://youtube.googleapis.com/youtube/v3/search?part=snippet&order=date&q=official&key=AIzaSyDCa32_gehikY8wO2EOm3kYStQE27aGXhA')
    
    if response.status_code == 200:
        response = response.json()["items"]
        # return JsonResponse(response, safe=False)

        return render(request, 'main/index.html', {'response': response})
    else:
        return render(request, 'main/index.html', {'response': response})
    


# def start(request):
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(show_latest_videos, 'interval', seconds=10)
#     scheduler.start()