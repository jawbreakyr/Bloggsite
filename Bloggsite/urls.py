from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

from articles import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Bloggsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^index/$', views.index, name='index'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.category),
    url(r'^(?P<category_slug>[-\w]+)/(?P<article_id>\d+)/([-\w]+)/$', views.article)
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
