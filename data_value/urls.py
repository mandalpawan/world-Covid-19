from django.urls import path,include
from .import views


urlpatterns = [
    #path('hello/',ClubCharView.as_view(),name="hello"),
    path('hello/',views.hello,name= 'hello'),
    path('hello/getdata/',views.getdata,name= 'getdata'),
]
