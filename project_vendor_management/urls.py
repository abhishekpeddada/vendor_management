from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/',include('api.urls')),
    path('', admin.site.urls),
    path('gettoken/', obtain_auth_token),
]
