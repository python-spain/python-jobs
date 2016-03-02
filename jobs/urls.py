from django.conf.urls import url

from .views import (
    PublishedListView, JobDetailView,
    JobByCategoryListView, JobByPlaceListView,
    JobCreate, JobUpdate, JobDelete
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
        r'job/add/$', JobCreate.as_view(), name='job-create'
    ),
    url(
        r'job/edit/(?P<slug>[-\w]+)/$', JobUpdate.as_view(), name='job-update'
    ),
    url(
        r'job/delete/(?P<slug>[-\w]+)/$', JobDelete.as_view(), name='job-delete'
    ),
]
