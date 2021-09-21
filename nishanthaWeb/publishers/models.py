from django.db import models

class Publisher(models.Model):
    title = models.CharField(max_length=100)
    title_sinhala = models.CharField(max_length=250, default=" ")
    logo = models.ImageField(upload_to="publishers/logo", blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    land_tel = models.CharField(max_length=11, blank=True, null=True, default="")
    tel1 = models.CharField(max_length=11, blank=True, null=True, default="")
    tel2 = models.CharField(max_length=11, blank=True, null=True, default="")

    def __str__(self):
        return self.title