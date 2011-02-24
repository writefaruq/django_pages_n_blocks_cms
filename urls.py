from django.conf.urls.defaults import *
from django.views.static import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
     (r'^', include('static_pages.urls')),
    # Required to make static serving work
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    #(r'^pages/pages/home', 'static_pages.views.home_view'),
    #(r'^pages/(?P<page_name>)', 'static_pages.views.page_view'),
    #(r'^pages/(?P<page_name>)', 'static_pages.views.page_view'),
)


