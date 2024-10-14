# Owned by Yash Jangid 
# github_id = im-yash21
# leetcode_id = im-yash21
# linkeldn_id = im-yash21 

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from gallery.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('add/',add),
    path('delete/<id>/',delete),
    path('register/',register),
    path('login/',login_page),
    path('logout/',logout_page)
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
