from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    year = models.IntegerField()
    engine = models.CharField(max_length=50)
    color = models.CharField(max_length=50) 
    discount = models.IntegerField(default=0)

    def get_discounted_price(self):
        return float(self.price) * (1 - float(self.discount)/100)
    
    def __str__(self):
        return f"{self.name} ({self.year})"

class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)