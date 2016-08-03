from django.conf.urls import *
from portal.views import *

urlpatterns = [

    # Main web portal entrance.
    url(r'^$', portal_main_page),

]