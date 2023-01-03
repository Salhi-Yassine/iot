from . import views
from app import views
from app import api
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.dht, name='Data'),
    path('charts/', views.EditorChartView.as_view(), name='CH'),
    path('temp/', views.temperature, name='temperature'),
    path('csv/', views.exp_csv, name='exp-csv'),
    path('api/list', api.Dlist, name='DHT11List'),
    path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
]
