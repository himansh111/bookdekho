from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'course.views.home', name='home'),
     url(r'^books/(?P<id>[0-9]+)/$', 'course.views.books', name='books'),
     url(r'^home/', 'course.views.home', name='home'),
     url(r'^books/', 'category.views.books', name='books'),

     url(r'^contact/', 'course.views.contact', name='contact'),
     #url(r'^booklist/(?P<id>[0-9]+)/$', 'category.views.books', name='booklist'),
     url(r'^bookslist/(?P<id>[0-9]+)/$', 'course.views.bookslist', name='booklist'),
     url(r'^novels/', 'novel.views.novels', name='novel'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', 'course.views.auth_view', name='auth_view'),
    url(r'^profile/', 'course.views.profile', name='profile'),
    url(r'^login/$', 'course.views.user_login', name='user_login'),
    url(r'^logout/$', 'course.views.user_logout', name='user_logout'),
) +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
