from django.contrib.sites import requests
from django.http import JsonResponse, HttpRequest
import json
# Create your views here
from django.shortcuts import redirect

config = json.load(open('config.json'))

oauth2redirect = "https://discord.com/api/oauth2/authorize?client_id=739898900294664205&redirect_uri=http%3A%2F" \
                 "%2Flocalhost%3A8000%2Foauth%2Fredirect&response_type=code&scope=identify%20guilds "

def home(request: HttpRequest):
    return JsonResponse({ "status": "Online..."})

def oauth(request: HttpRequest):
    return redirect(oauth2redirect)


def oauth_redirect(request: HttpRequest):
    code = request.GET.get("code")
    print(code)
    data = {
        "client_id": config["clientID"],
        "client_secret": config["clientSecret"],
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/oauth/redirect",
        "scope": "identify"
    }
    headers = {
        'Content Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    print(response.json())
    return JsonResponse({"msg": "hi"})
