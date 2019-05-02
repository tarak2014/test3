from django.db import models

# Create your models here.
class Notes(models.Model):
    notes = models.CharField(max_length=300)
    title = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)