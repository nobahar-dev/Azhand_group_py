from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Project Apps Urls
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('home.urls', namespace='home')),
    path('avicenna/', include('avicenna.urls', namespace='avicenna')),
    path('arasto/', include('arasto.urls', namespace='arasto')),
    path('informatics/', include('informatics.urls', namespace='informatics')),
    path('safety/', include('safety.urls', namespace='safety')),
    path('office/', include('office.urls', namespace='office')),
    path('human/', include('human.urls', namespace='human')),
    path('ticketing/', include('ticketing.urls', namespace='ticketing')),
    # Custom Apps Url
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)