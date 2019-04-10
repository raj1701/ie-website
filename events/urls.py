from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from events import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'events'

urlpatterns = [
    url(r'^events/$', views.view_events, name='events'),
    path('smp2019/', views.smp, name='smp'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
