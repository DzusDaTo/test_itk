from django.db import models


class BaseStation(models.Model):
    ne = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255)  # Координаты как строка
    technology = models.CharField(max_length=255)  # Строка для технологий
    status = models.BooleanField()

    def __str__(self):
        return self.ne
