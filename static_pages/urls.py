from django.conf.urls.defaults import *
from views import home_view

urlpatterns = patterns(' ',
                       url(r'^$', home_view),
                       url(r'index.html', home_view),
#                       url(r'member_login', login_view),
#                       url(r'member_logout', logout_view),
#                        url(r'search', search_view),
)


