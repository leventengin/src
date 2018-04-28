from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse

# django hosts --> subdomain for reverse

class BlogPost(models.Model):
    # pk aka id --> numbers
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title       = models.CharField(max_length=120, null=True, blank=True)
    content     = models.TextField(max_length=120, null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def owner(self):
        return self.user
    # def get_absolute_url(self):
    #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'

    def get_api_url(self, request=None):
        return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)


class MacPost(models.Model):
    # pk aka id --> numbers
    mac_no      = models.CharField(max_length=20)
    timestamp   = models.DateTimeField()

    def __str__(self):
        return str(self.mac_no)

    @property
    def owner(self):
        return self.mac_no


    def get_api_url(self, request=None):
        return api_reverse("api-postings:mac-rud", kwargs={'pk': self.pk}, request=request)


class Memnuniyet(models.Model):
    mac_no      = models.CharField(max_length=20)
    tipi        = models.CharField(max_length=2)
    oy          = models.CharField(max_length=1)
    sebep       = models.CharField(max_length=2)
    gelen_tarih = models.CharField(max_length=30)
    timestamp   = models.DateTimeField()

    def __str__(self):
        return str(self.mac_no)

    @property
    def owner(self):
        return self.mac_no

    def get_api_url(self, request=None):
        return api_reverse("api-postings:memnuniyet-rud", kwargs={'pk': self.pk}, request=request)
