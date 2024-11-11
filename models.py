from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Убедитесь, что имя уникально
    age = models.IntegerField()
