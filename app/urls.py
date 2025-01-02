from xml.etree.ElementInclude import include
from django.urls import path
from .views import HomepageView, AboutpageView, ResidentListView, ResidentDetailView, ResidentCreateView, ResidentUpdateView, ResidentDeleteView

urlpatterns = [
    path('', HomepageView.as_view(), name='Home'),
    path('About/', AboutpageView.as_view(), name='About'),
    path('post_list/', ResidentListView.as_view(), name='Record'),
    path('post_detail/<int:pk>', ResidentDetailView.as_view(), name='post_detail'),
    path('post_Create', ResidentCreateView.as_view(), name='post_create'),
    path('post_detail/<int:pk>/edit>', ResidentUpdateView.as_view(), name='post_update'),
    path('post_detail/<int:pk>/delete>', ResidentDeleteView.as_view(), name='post_delete'),
]
