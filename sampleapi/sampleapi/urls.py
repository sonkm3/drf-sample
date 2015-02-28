from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from api import views

api_router = DefaultRouter()
api_router.register(r'temp', views.TempViewSet, base_name = 'temp_view')
api_router.register(r'simplereadwrite', views.SimpleReadWriteViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sampleapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(api_router.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
