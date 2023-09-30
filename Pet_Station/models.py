from django.db import models

import Outsider


# Create your models here.


class Categories(models.Model):
    category_name=models.CharField(max_length=100)
    category_image=models.ImageField(upload_to='images/',max_length=500)
    category_status=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

GENDER_CHOICE=[
    ('female','Female'),
    ('male','Male'),
    ('pair','Pair')
]

class PetData(models.Model):
    categoryId=models.ForeignKey(Categories,on_delete=models.CASCADE)
    categoryName=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    breed=models.CharField(max_length=200)
    age=models.CharField(max_length=100)
    gender=models.CharField(choices=GENDER_CHOICE,max_length=100)
    price=models.CharField(max_length=200)
    description=models.CharField(max_length=800)
    rating=models.FloatField(max_length=100,null=True,default=0.0)
    rating_count=models.IntegerField(default=0,null=True)
    image1=models.ImageField(upload_to='images/',max_length=500,null=True)
    image2=models.ImageField(upload_to='images/',max_length=500,null=True)
    image3=models.ImageField(upload_to='images/',max_length=500,null=True)
    image4=models.ImageField(upload_to='images/',max_length=500,null=True)
    expdate=models.CharField(max_length=200,default='10')
    petstatus=models.CharField(max_length=100)

class Food(models.Model):
    categoryId=models.ForeignKey(Categories,on_delete=models.CASCADE)
    categoryName=models.CharField(max_length=200)
    product_name=models.CharField(max_length=1100)
    product_type=models.CharField(max_length=500)
    net_weight=models.CharField(max_length=400)
    company_name=models.CharField(max_length=1800)
    benefit=models.CharField(max_length=1800)
    price=models.CharField(max_length=200)
    marketed_by=models.CharField(max_length=1800)
    description=models.CharField(max_length=2000)
    expdate=models.CharField(max_length=200)
    image1=models.ImageField(upload_to='images/',max_length=500,null=True)
    image2=models.ImageField(upload_to='images/',max_length=500,null=True)
    image3=models.ImageField(upload_to='images/',max_length=500,null=True)
    image4=models.ImageField(upload_to='images/',max_length=500,null=True)
    image5=models.ImageField(upload_to='images/',max_length=500,null=True)
    rating=models.FloatField(max_length=100,null=True,default=0.0)
    rating_count=models.IntegerField(default=0,null=True)
    foodstatus=models.CharField(max_length=100)

class Notifications(models.Model):
    user=models.ForeignKey('Outsider.outsiders',on_delete=models.CASCADE)
    order=models.ForeignKey('Outsider.Order',on_delete=models.CASCADE)
    notification_content=models.CharField(max_length=1800)
    notification_title=models.CharField(max_length=800)
    date=models.CharField(max_length=800)
    notification_status=models.CharField(max_length=100)


