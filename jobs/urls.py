from django.conf.urls import url

from .views import (
    PublishedListView, JobPostDetailView,
    JobByCategoryListView, JobByPlaceListView
)

urlpatterns = [
    url(r'^published/', PublishedListView.as_view()),
    url(r'^category/(?P<slug>[-\w]+)/$', JobByCategoryListView.as_view()),
    url(r'^place/([0-9]+)/$', JobByPlaceListView.as_view()),
    url(
        r'^(?P<slug>[-\w]+)/$', JobPostDetailView.as_view(), name='job-detail'
    ),
]
