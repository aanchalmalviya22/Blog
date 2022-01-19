from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Tag(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class Post(models.Model):
    STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published'),
        ('ARCHIEVED', 'Archieved')
    )


    title = models.TextField(max_length=125)
    content = models.TextField(max_length=100)
    summary = models.TextField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=125)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, related_name="posts")
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='DRAFT')
    created_ad = models.DateTimeField(auto_now_add=True)
    modified_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-modified_ad"]




