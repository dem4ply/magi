from django.conf.urls import url, include
from django.contrib import admin

from papernews.urls import urlpatterns as papernews_url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url( r'papernews/', include( papernews_url, namespace='pepernews' ), ),
]
