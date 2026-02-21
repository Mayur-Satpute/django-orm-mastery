from django.db import models

#Restaurant model
#User model
#Rating model

class Restaurant(models.Model):
    name = models.CharField(max_lenght=255)
    
