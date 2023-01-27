from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
    path('', include('mycart.urls')),
    path('', include('user.urls')),

]


urlpatterns += staticfiles_urlpatterns()

