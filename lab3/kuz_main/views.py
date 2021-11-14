from django.shortcuts import render
from django.http import JsonResponse
import requests
import os
from datetime import datetime


def main(request):
    return render(request, 'kuz_main.html', {'parameter': "kuz_test"})


def health(request):
    response = {'date': datetime.now(), 'current_page': request.get_host() + request.get_full_path(), 'server_info': os.uname(),
                'client_info': request.headers['User-Agent']}
    return JsonResponse(response)
