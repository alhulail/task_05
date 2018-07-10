from django.shortcuts import render
from .models import Restaurant

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    context = {
        "object_list": restaurants,
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    restaurants = Restaurant.objects.get(id=restaurant_id)
    context = {
        "object_detail": restaurants,
    }
    return render(request, 'detail.html', context)
