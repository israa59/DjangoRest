from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self) -> str:
        return self.id+self.name+self.salary
