
from django.contrib import admin
from django.urls import path,include
from apps.users.views import Login,Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/',include('apps.users.api.urls')),
    path('',Login.as_view(), name = 'Login'),
    path('Logout/', Logout.as_view(), name = 'Logout'),
]
