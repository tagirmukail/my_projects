from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url для приложения users
    url(r'^users/', include('users.urls', namespace='users')),
    # url для приложения journal.
    url(r'', include('journal.urls', namespace='journal')),

]
