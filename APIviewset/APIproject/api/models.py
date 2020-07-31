from django.db import models

# Create your models here.
class Staff(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    address=models.CharField(max_length=255)
    salary=models.IntegerField()

    def __str__(self):
        return self.name