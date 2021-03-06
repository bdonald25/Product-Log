from django.conf.urls import patterns, include, url, static
from django.conf.urls.static import static
from dansdb import settings

from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dansdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('products.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
