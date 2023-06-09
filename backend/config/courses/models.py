from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


