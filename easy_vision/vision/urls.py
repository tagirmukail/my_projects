from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BlogList, name='BlogList'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='RegisterFormView'),
    url(r'^login/$', views.LoginFormView.as_view(), name='LoginFormView'),
    url(r'logout/$', views.LogoutView.as_view(), name='LogoutView'),
    url(r'^search/$', views.SearchListView.as_view(), name='search'),
    url(r'^create/$', views.create_blogpost, name='Create'),
    url(r'^call', views.contactView, name='ContactView'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.BlogList, name='BlogListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.BlogDetail, name='BlogDetail'),
]
