from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('new_place/', views.get_new_place, name='get_new_place'),
    path('map/', views.gmap, name='map'),
]
