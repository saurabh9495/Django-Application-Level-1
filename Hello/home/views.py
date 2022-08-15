from multiprocessing import context
from django.shortcuts import render, HttpResponse
import requests
import random
# Create your views here.


def index(request):

    url = "https://api.unsplash.com/search/photos?page=" + \
        str(random.randint(1, 100)) + \
        "&query=girl&client_id=1ZIf-xckVpzX5RWlYQ-IUGym-4Q6a3En8JVs3zciX_Y"

    payload = {}
    headers = {
        'Cookie': 'ugid=42bbb2992106803b518bbc71da8f1e395535305'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()

    context = {}
    for key, value in enumerate(data['results']):
        # print(value['urls']['full'])
        context["variable"+str(key)] = value['urls']['raw']

    # print(context)

    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services")


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is contact")
