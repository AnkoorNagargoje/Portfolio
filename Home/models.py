from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=1000)


BLOG_TYPE = (
    ('Startups', 'Startups'),
    ('Web Development', 'Web Development'),
    ('My Journey', 'My Journey'),
    ('Django', 'Django'),
    ('Social Media', 'Social Media'),
)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    type = models.CharField(choices=BLOG_TYPE, max_length=100, default='My Journey')
    read_time = models.PositiveIntegerField(default=0)
    image_url = models.CharField(max_length=100)
    time = models.DateTimeField(auto_created=True, auto_now=True)
