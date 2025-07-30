from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Akila.urls')),  # replace 'yourapp' with your Django app name
]
