from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

from rest_framework.routers import DefaultRouter
from api import views

api_router = DefaultRouter()
api_router.register(r'temp', views.TempViewSet, base_name = 'temp_view')
api_router.register(r'simplereadwrite', views.SimpleReadWriteViewSet)
api_router.register(r'item', views.ItemViewSet)
api_router.register(r'imagestore', views.ImageStoreViewSet)

api_router.register(r'fieldsamplefull', views.FieldSampleFullViewSet, base_name = 'fieldsamplefull')
api_router.register(r'fieldsampleminimum', views.FieldSampleMinimumViewSet, base_name = 'fieldsampleminimum')

api_router.register(r'mixineditem', views.MixinedItemViewSet, base_name = 'mixeineditem')
api_router.register(r'modelviewsetitem', views.ModelViewSetItemViewSet, base_name = 'modelviewsetitem')
api_router.register(r'itemserializerwithsource', views.ItemSerializerWithSourceViewSet, base_name = 'item_serializer_with_source')

api_router.register(r'serializermethodfield', views.SerializerMethodFieldViewSet, base_name = 'serializer_method_field')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sampleapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(api_router.urls)),

    url(r'^admin/', include(admin.site.urls)),

    # ImageFieldのファイルの配信
    url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),


)
