from django.db import models

# Create your models here.
class carModel(models.Model):
    make = models.CharField(max_length=15, default="")
    model = models.CharField(max_length=25, default="")
    year = models.IntegerField(max_length=4, default="")
    milesPerGallon = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.make