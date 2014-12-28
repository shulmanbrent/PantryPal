from django.conf.urls import patterns, include, url
from django.contrib import admin
from PantryPal import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PantryPal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^PantryPal_app/', include('PantryPal_app.urls')),
)

urlpatterns += patterns('',
    (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
)
