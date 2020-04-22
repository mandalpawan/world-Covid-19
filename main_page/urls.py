from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('update/',views.update,name='update'),
    path('feedback/',views.feedback,name='feedback'),
     path('payment', views.payment, name="payment"),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
    path('graph/',views.graph,name='graph'),
    path('map_dire/',views.map_dire,name='map_dire'),
    path('save_data/',views.save_data,name='save_data'),
]
