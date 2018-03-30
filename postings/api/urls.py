from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import BlogPostRudView, BlogPostAPIView, BlogPostDestroyView, BlogPostDetailView
from .views import MacPostRudView, MacList, MacDetail, MacPostDetailView

urlpatterns = [
    url(r'^$', BlogPostAPIView.as_view(), name='post-listcreate'),
    url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name='post-rud'),
    url(r'^destroy/(?P<pk>\d+)/$', BlogPostDestroyView.as_view(), name='post-destroy'),
    url(r'^bul/(?P<pk>\d+)/$', BlogPostDetailView.as_view(), name='bul_event'),
    url(r'^bul/delete/(?P<pk>\d+)/$', BlogPostDetailView.as_view(), name='delete_event'),
    url(r'^mac_list/$', MacList.as_view(), name='mac_list'),
    url(r'^mac_detail/(?P<pk>[0-9]+)/$', MacDetail.as_view(), name='mac-rud'),
    #url(r'^mac/(?P<pk>\d+)/$', MacPostDetailView.as_view(), name='mac-rud'),
]


#url(r'^denetim/(?P<pk>\d+)/update/$', views.DenetimUpdate.as_view(), name='denetim_update'),
