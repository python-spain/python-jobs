from django.db import models
from cities_light.models import City


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class JobPost(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True, editable=False)
    published_at = models.DateField(null=True, blank=True, default=None)
    slug = models.SlugField(max_length=255, blank=True, default='')
    description = models.TextField()
    requirements = models.TextField()
    about_the_company = models.TextField()
    contact_email = models.EmailField()
    contact_person = models.CharField(max_length=255)
    web_page = models.URLField(max_length=255, blank=True, default='')
    times_viewed = models.IntegerField(default=0)
    category = models.ForeignKey(Category, related_name='job_posts')
    place = models.ForeignKey(
        City, related_name='job_posts', blank=True, null=True
    )

    def __str__(self):
        return "%s @ %s" % (self.title, self.place)
