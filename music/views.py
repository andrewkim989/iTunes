from django.shortcuts import render, HttpResponse
import requests

def home(request):
    return render(request, "home.html")

def getmusic(request):
    artist = request.POST["artist"].replace(" ", "")
    url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"

    response = requests.get(url).content
    return HttpResponse(response, content_type = "application/json")