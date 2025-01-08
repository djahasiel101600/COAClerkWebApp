from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name='rci-index'),
    path('load-rci-data/', views.loadRCIData, name='load-rci-data'),
    path('post-data-endpoint/<str:fund>/', views.postdataendpoint),
    path('listview/', views.listView, name='rci-listview')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)