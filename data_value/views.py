from django.shortcuts import render,redirect
from covid import Covid
from .models import Club
from .models import Country
from django.http import JsonResponse
from django.views.generic import TemplateView


def hello(request):
    return render(request,'hello.html')

def getdata(request):
    club_data = []
    context = Club.objects.all()
    for item in context:
        club_data.append({item.name:item.money})
    return JsonResponse(club_data,safe=False)

