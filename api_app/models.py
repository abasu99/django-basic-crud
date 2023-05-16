from django.db import models


# Create your models here.
class Car(models.Model):

    car_id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)

    def __str__(self):
        return self.model_name
