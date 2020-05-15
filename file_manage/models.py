from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 50)
    date_of_birth = models.DateField()
    ref = models.CharField(max_length = 10)
    def get_absolute_url(self):
        return reverse("customer_info", kwargs={'pk':self.pk})

    def __str__(self):
        return self.ref