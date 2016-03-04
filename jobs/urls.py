from django.conf.urls import url

from .views import (
    PublishedListView, JobDetailView, JobPublishView,
    JobByCategoryListView, JobByPlaceListView,
    JobCreateView, JobUpdateView, JobDeleteView
)

urlpatterns = [
    url(
        r'published/',
        PublishedListView.as_view(), name='jobs-published'
    ),
    url(
        r'category/(?P<slug>[-\w]+)/$',
        JobByCategoryListView.as_view(), name='jobs-by-category'
    ),
    url(
        r'place/([0-9]+)/$',
        JobByPlaceListView.as_view(), name='jobs-by-place'
    ),
    url(
        r'^(?P<slug>[-\w]+)/$',
        JobDetailView.as_view(), name='job-detail'
    ),
    url(
        r'job/add/$', JobCreateView.as_view(), name='job-create'
    ),
    url(
        r'job/publish/(?P<slug>[-\w]+)/$', JobPublishView.as_view(), name='job-publish'
    ),
    url(
        r'job/edit/(?P<slug>[-\w]+)/$', JobUpdateView.as_view(), name='job-update'
    ),
    url(
        r'job/delete/(?P<slug>[-\w]+)/$', JobDeleteView.as_view(), name='job-delete'
    ),
]
