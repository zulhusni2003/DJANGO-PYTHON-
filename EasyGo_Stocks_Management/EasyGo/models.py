from django.db import models

# Create your models here.

class Staff(models.Model):
    staffID = models.CharField(max_length=10, primary_key=True)
    staffName = models.TextField(max_length=100)
    staffPhoneNumber = models.CharField(max_length=11)
    staffPassword = models.CharField(max_length=9, default='null')
    
class Product(models.Model):
    productID = models.CharField(max_length=4, primary_key=True)
    productName = models.TextField(max_length=100)
    productPrice = models.FloatField()
    productQuantity = models.IntegerField()
    productExpirationDate = models.DateField() 
    
class FaQ(models.Model):
    faqID = models.CharField(max_length=3, primary_key=True)
    
class FaQ_management(models.Model):
    faqID = models.ForeignKey(FaQ, on_delete=models.CASCADE, null=True)
    staffID = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    question = models.TextField(null=True)
    
class Stock_management(models.Model):
    staffID = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    stockIn = models.TextField(null=True)
    stockOut = models.TextField(null=True)
    

      