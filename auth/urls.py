
from django.contrib import admin
from django.urls import path, include
from users import views
# from . import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),

]
