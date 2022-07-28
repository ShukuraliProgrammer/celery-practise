from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(default=0)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Contact'
        verbose_name_plural = "Contacts"
