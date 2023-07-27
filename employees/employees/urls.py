from django.contrib import admin
from django.urls import path

from data.views import download_data

urlpatterns = [
    path('', download_data, name='download_data'),
    path('admin/', admin.site.urls),
]
