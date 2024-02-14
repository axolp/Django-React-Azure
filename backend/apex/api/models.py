from django.db import models

class fiszka(models.Model):
    character= models.TextField()
    sentence= models.TextField()
    wideo_second= models.IntegerField()
