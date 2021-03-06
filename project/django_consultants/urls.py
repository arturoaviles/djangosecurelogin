"""django_consultants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    # Main Page
    url(r'^$', views.main_page),
    
    # Login / logout.
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),

    # Web portal.
    url(r'^portal/', include('portal.urls')),

    # Serve static content.
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
]
