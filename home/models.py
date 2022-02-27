from django.db import models

class NewsletterEmail(models.Model):
    email = models.EmailField(max_length=60)

    def __str__(self):
        return str(self.email)