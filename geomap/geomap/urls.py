from django.conf import settings
from django.conf.urls import url, include
from django.contrib.gis import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('worldmap.urls', namespace='worldmap')),
]
