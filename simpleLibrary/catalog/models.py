from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=250)
    author=models.CharField(max_length=250, blank=True)
    publish_date=models.DateField(blank=True)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title

    def save_book(self):
        return self.save()

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})
