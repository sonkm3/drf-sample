from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

from rest_framework.routers import DefaultRouter
from api import views

api_router = DefaultRouter()
api_router.register(r'temp', views.TempViewSet, base_name = 'temp_view')
api_router.register(r'simplereadwrite', views.SimpleReadWriteViewSet, base_name = 'simple_read_write')
api_router.register(r'item', views.ItemViewSet, base_name='item')
api_router.register(r'imagestore', views.ImageStoreViewSet, base_name='imagestore')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sampleapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(api_router.urls)),

    # ImageFieldのファイルの配信
    url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),

    url(r'^admin/', include(admin.site.urls)),
)
