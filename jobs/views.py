from django.contrib.syndication.views import Feed
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from datetime import date

from cities_light.models import City

from .forms import JobForm
from .models import Job, Category


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    queryset = Job.objects.filter(published_at__isnull=False)

    def get_object(self):
        # Call the superclass
        object = super(JobDetailView, self).get_object()
        # Increment and save the number of views
        object.last_viewed_at = date.today()
        object.times_viewed += 1
        object.save()
        # Return the object
        return object


class PublishedListView(ListView):
    model = Job
    queryset = Job.objects.filter(published_at__isnull=False)

    def head(self, *args, **kwargs):
        last_published = self.get_queryset().latest('published_at')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_published.published_at.strftime(
            '%a, %d %b %Y %H:%M:%S GMT'
        )
        return response

    def get_context_data(self, **kwargs):
        context = super(PublishedListView, self).get_context_data(**kwargs)
        context['titlepage'] = "Published"
        return context


class PublishedJobsFeed(Feed):
    title = "Python Spain Jobs Feed"
    link = "/published/"
    description = "Updates on changes and additions to Python Spain Jobs."

    def items(self):
        return Job.objects.order_by('-published_at')[:20]

    def item_title(self, item):
        return "%s (%s)" % (item.title, item.company)

    def item_description(self, item):
        return item.description


class CategoryFeed(Feed):

    def get_object(self, request, slug):
        return Category.objects.get(slug=slug)

    def title(self, obj):
        return "Jobs for category: %s" % obj.name

    def link(self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return "Jobs recently posted in category: %s" % obj.name

    def items(self, obj):
        return Job.objects.filter(
            category=obj,
            published_at__isnull=False
        ).order_by('-published_at')[:10]


class PlaceFeed(Feed):

    def get_object(self, request, place_id):
        return City.objects.get(pk=place_id)

    def title(self, obj):
        return "Jobs for city: %s" % obj.name

    def link(self, obj):
        return reverse_lazy('jobs-by-place', args=[obj.pk])

    def description(self, obj):
        return "Jobs recently posted in city: %s" % obj.name

    def items(self, obj):
        return Job.objects.filter(
            place=obj,
            published_at__isnull=False
        ).order_by('-published_at')[:10]


class JobByCategoryListView(ListView):
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Job.objects.filter(
            category=self.category,
            published_at__isnull=False
        )

    def get_context_data(self, **kwargs):
        context = super(JobByCategoryListView, self).get_context_data(**kwargs)
        context['titlepage'] = "categorized as %s" % self.category
        return context


class JobPublishView(UserPassesTestMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'job_form.html'

    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, *args, **kwargs):
        response = super(JobPublishView, self).post(request, *args, **kwargs)
        job = Job.objects.get(**kwargs)
        job.published_at = date.today()
        job.save()
        return response


class JobByPlaceListView(ListView):
    def get_queryset(self):
        self.place = get_object_or_404(City, pk=self.args[0])
        return Job.objects.filter(
            place=self.place,
            published_at__isnull=False
        )

    def get_context_data(self, **kwargs):
        context = super(JobByPlaceListView, self).get_context_data(**kwargs)
        context['titlepage'] = "to work in %s" % self.place
        return context


class JobCreateView(CreateView):
    form_class = JobForm
    template_name = 'job_form.html'


class JobUpdateView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'job_form.html'


class JobDeleteView(DeleteView):
    model = Job
    success_url = reverse_lazy('jobs-published')
