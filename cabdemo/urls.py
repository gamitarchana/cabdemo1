from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
#from comments import views as reviews_views
from reviews import views as reviews_views
from login import views as login_views
from outstation import views as outstation_views

from .api import api_router

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),
    url(r'^login/$', login_views.login, name='login'),
    #url(r'^reviews/$', reviews_views.reviews, name='reviews'),

    #url(r'^photo-upload/$', location_views.photo_upload, name='photo_upload'),
    url(r'^like/$', outstation_views.like_route, name='like_route'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    #url(r'^routelike/$', outstation_views.route_like, name='route_like'),
    #url(r'^photoupload/$', reviews_views.photoupload, name='photoupload'),
    #url(r'^photos/$', reviews_views.photos, name='photos'),
    #url(r'^reviewlist/$', reviews_views.review_list, name='review_list'),
    url(r'^reviewlist/(?P<route_id>[0-9]+)/$', reviews_views.review_list, name='review_list'),
    #url(r'^reviewImagelist/(?P<review_id>[0-9]+)/$', reviews_views.review_image_list, name='review_image_list'),
    url(r'^review/$', reviews_views.review, name='review'),

    #url(r'^routePage/$', reviews_views.route_page, name='route_page'),
    url(r'^api/v2/', api_router.urls),
    #url(r'^submit-review/$', location_views.submit_review, name='submit_review'),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
