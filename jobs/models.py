from django.db import models
from django.core.urlresolvers import reverse
from cities_light.models import City


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(
        max_length=255, unique=True, blank=True, default=''
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jobs-by-category', kwargs={'slug': self.slug})


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True, editable=False)
    published_at = models.DateField(null=True, blank=True, default=None)
    last_viewed_at = models.DateField(editable=False)
    times_viewed = models.IntegerField(default=0)
    slug = models.SlugField(
        max_length=255, unique=True, blank=True, default=''
    )
    description = models.TextField()
    requirements = models.TextField()
    about_the_company = models.TextField()
    contact_email = models.EmailField()
    contact_person = models.CharField(max_length=255)
    web_page = models.URLField(max_length=255, blank=True, default='')
    category = models.ForeignKey(Category, related_name='jobs')
    place = models.ForeignKey(
        City, related_name='jobs', blank=True, null=True
    )

    def __str__(self):
        return "%s @ %s" % (self.title, self.place)

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'slug': self.slug})
