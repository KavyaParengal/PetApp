from django.db import models

# Create your models here.


class Categories(models.Model):
    category_name=models.CharField(max_length=100)
    category_image=models.ImageField(upload_to='images/',max_length=500)
    category_status=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

GENDER_CHOICE=[
    ('female','Female'),
    ('male','Male')
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
    rating=models.CharField(max_length=100,null=True)
    image1=models.ImageField(upload_to='images/',max_length=500,null=True)
    image2=models.ImageField(upload_to='images/',max_length=500,null=True)
    image3=models.ImageField(upload_to='images/',max_length=500,null=True)
    image4=models.ImageField(upload_to='images/',max_length=500,null=True)
    petstatus=models.CharField(max_length=100)



