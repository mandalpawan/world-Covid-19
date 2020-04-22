from django.shortcuts import render
from main_page.models import Crona_data
from django.http import JsonResponse

# Create your views here.
def pre_map_home(request):
    covid_data = Crona_data.objects.all()
    return render(request,'pre_home_map.html',{'covid_data':covid_data})

def map_home(request,country_name):
    return render(request,'map_home.html',{'covid_data':country_name})

#Sending Total case data
def map_data(request,obj):
    country_data = []
    context = Crona_data.objects.filter(country__iexact=obj)
    for item in context:
        #Total Case
        myData = item.total_case
        myDataUpdate = myData.replace(',', '')
        # Date Update
        myDate = item.update_date
        myDate_update = myDate.strftime("%b-%d ")
        country_data.append({str(myDate_update):myDataUpdate})
        
    return JsonResponse(country_data, safe=False)

#Sending Recovery data 
def map_datarec(request,obj):
    country_data = []
    context = Crona_data.objects.filter(country__iexact=obj)
    for item in context:
        #Total Recovery Case
        myData = item.total_recovery
        myDataUpdate = myData.replace(',', '')
        #date update 
        myDate = item.update_date
        myDate_update = myDate.strftime("%b-%d ")
        country_data.append({str(myDate_update):myDataUpdate})
        
    return JsonResponse(country_data, safe=False)

#Sending Death data 
def map_datadet(request,obj):
    country_data = []
    context = Crona_data.objects.filter(country__iexact=obj)
    for item in context:
        #Total Recovery Case
        myData = item.total_death
        myDataUpdate = myData.replace(',', '')
        #date update 
        myDate = item.update_date
        myDate_update = myDate.strftime("%b-%d ")
        country_data.append({str(myDate_update):myDataUpdate})
    return JsonResponse(country_data, safe=False)