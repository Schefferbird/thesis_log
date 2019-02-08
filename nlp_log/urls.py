"""nlp_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import LoginView, RegisterView
from django.views.static import serve
from django.views.generic import RedirectView

from .views import about_page, contact_page, faq_page, home_page



urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^api/', include('log.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include("accounts.passwords.urls")),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^settings/$', RedirectView.as_view(url='/account')),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^faq/$', faq_page, name='faq'),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root' : settings.MEDIA_ROOT,
        }),
    ]