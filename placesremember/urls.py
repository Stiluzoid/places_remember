from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('places/', include('places.urls')),
    path('', views.index, name='index'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]