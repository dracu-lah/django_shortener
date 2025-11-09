from django.db import models
import uuid


class Link(models.Model):
    shortened = models.SlugField(max_length=40, unique=True, db_index=True)
    long_url = models.URLField()
    email = models.EmailField(db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.shortened} -> {self.long_url}"
