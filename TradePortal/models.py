from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10, unique=True, null=True)
    scripcode = models.IntegerField(unique=True, null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "Companies"


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Watchlist: {self.company.symbol}"

    class Meta:
        unique_together = ('user', 'company')


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()