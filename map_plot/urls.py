from django.urls import path,include
from .import views


urlpatterns = [
    path('pre_map_home/',views.pre_map_home,name='pre_map_home'),
    path('map_home/<str:country_name>',views.map_home,name='map_home'),
    path('map_data/<str:obj>/',views.map_data,name='map_data'),
    path('map_datarec/<str:obj>/',views.map_datarec,name='map_datarec'),
    path('map_datadet/<str:obj>/',views.map_datadet,name='map_datadet'),
]
