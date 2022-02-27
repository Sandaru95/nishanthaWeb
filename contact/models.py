from django.db import models

class ContactMessage(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_tel = models.CharField(max_length=11)
    sender_message = models.TextField(max_length=500)

    def __str__(self):
        return f"{str(self.sender_name)} : {str(self.sender_tel)}"