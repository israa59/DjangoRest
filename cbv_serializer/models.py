from django.db import models

class StudentC(models.Model):
    name = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=20,  decimal_places=2)

    def __str__(self):
        return self.name