from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import datetime


class AnnualSalary(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(datetime.date.today().year)])
    economic_activity = models.CharField(max_length=500)
    total = models.IntegerField()
