from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

class Artikel(models.Model):
    penulis = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    judul = models.CharField(max_length = 200)
    isi = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)

    def get_absolute_url(self):
        return reverse('blog:details', args=[str(self.id)])

    def __str__(self):
        return self.judul