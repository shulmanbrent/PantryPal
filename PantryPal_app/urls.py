from django.conf.urls import patterns, url
from PantryPal_app import views
from PantryPal import settings

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),

)