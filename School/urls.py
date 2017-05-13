from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'School'

urlpatterns = [
    url(r'^$', views.index_view, name='home'),
    url(r'^gallery/', views.gallery_view, name='gallery'),
    url(r'^portal/', views.portal_view, name='portal'),
    url(r'^contacts/', views.contacts_view, name='contacts'),
    url(r'^about/', views.contacts_view, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


