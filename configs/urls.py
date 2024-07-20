from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myshop.urls')),
    path('users/', include('users.urls')),

    # third-party apps
    path('__debug__/', include('debug_toolbar.urls')),

    # Proxy paths
    path('hltuz/', RedirectView.as_view(url='https://hlt-asal.tilda.ws/hltuz', permanent=True), name='hltuz_proxy'),
    path('hlt5/', RedirectView.as_view(url='https://hlt-asal.tilda.ws/hlt5', permanent=True), name='hlt5_proxy'),
    path('zextranewid5grija/', RedirectView.as_view(url='https://hlt-asal.tilda.ws/zextranewid5grija', permanent=True), name='zextranewid5grija_proxy'),
    path('zextranewid5artrit/', RedirectView.as_view(url='https://hlt-asal.tilda.ws/zextranewid5artrit', permanent=True), name='zextranewid5artrit_proxy'),
    path('zextranewid5suyak/', RedirectView.as_view(url='https://hlt-asal.tilda.ws/zextranewid5suyak', permanent=True), name='zextranewid5suyak_proxy'),
    path('zextraalsafia/', RedirectView.as_view(url='https://hlt-asal.tilda.ws/zextraalsafia', permanent=True), name='zextraalsafia_proxy'),
    path('drbeezee/', RedirectView.as_view(url='https://hlt-asal.tilda.ws/drbeezee', permanent=True), name='drbeezee_proxy'),
    path('tibomeduzbekistan/', RedirectView.as_view(url='https://hlt-asal.tilda.ws/tibomeduzbekistan', permanent=True), name='tibomeduzbekistan_proxy'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]
