from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import datetime


class AnnualSalary(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(datetime.date.today().year)])
    economic_activity = models.CharField(max_length=500)
    total = models.IntegerField()


class Salary(models.Model):
    year = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.year}: {self.amount}"

    def get_percentage_change(self, old_amount):
        return ((self.amount - old_amount) / old_amount) * 100


class Difference(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(datetime.date.today().year)])
    economic_activity = models.CharField(max_length=500)
    total = models.IntegerField()