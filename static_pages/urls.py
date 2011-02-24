from django.conf.urls.defaults import *
from views import home_view, page_view

urlpatterns = patterns(' ',
                       url(r'^$', home_view),
                       url(r'^pages/home', home_view),
                       url(r'index.html', home_view),
                       url(r'^pages/(?P<page_name>)', page_view),
#                       url(r'member_login', login_view),
#                       url(r'member_logout', logout_view),
#                        url(r'search', search_view),
)


