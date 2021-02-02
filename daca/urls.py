from django.contrib import admin
from django.urls import path, include
import dj_rest_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/', include('api.urls'))
]
