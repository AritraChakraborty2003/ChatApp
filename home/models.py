from django.db import models

# Create your models here.
class ChatRoom(models.Model):
    rName=models.TextField()
    rCode=models.TextField()