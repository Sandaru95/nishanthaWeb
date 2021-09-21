from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    name_sinhala = models.CharField(max_length=250, default=" ")
    address = models.CharField(max_length=500, blank=True, null=True)
    tel = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return self.name