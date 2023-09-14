from django.db import models

from Pet_Station.models import PetData

# Create your models here.

class Log(models.Model):
    usernmController=models.CharField(max_length=100,unique=True)
    pwdController=models.CharField(max_length=80,unique=True)
    role=models.CharField(max_length=10)
    def __str__(self):
        return self.usernmController
    
class outsiders(models.Model):
    fullnameController=models.CharField(max_length=100,unique=True)
    phoneController=models.CharField(max_length=100)
    emailController=models.EmailField(max_length=100,unique=True)
    usernmController=models.CharField(max_length=100)
    pwdController=models.CharField(max_length=80,unique=True)
    log_id=models.OneToOneField(Log,on_delete=models.CASCADE)
    role=models.CharField(max_length=10)
    userstatus=models.CharField(max_length=10)
    userimage=models.ImageField(upload_to='images',max_length=500,default='/meadia/images/user1.png')
    def __str__(self):
        return self.fullnameController
    
class Cart(models.Model):
    item=models.ForeignKey(PetData,on_delete=models.CASCADE)
    user=models.ForeignKey(outsiders,on_delete=models.CASCADE)
    itemname=models.CharField(max_length=500)
    breedname=models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    quantity = models.CharField(max_length=500)
    total_price=models.CharField(max_length=500)
    category = models.CharField(max_length=10)
    cart_status=models.CharField(max_length=10)

class OrderAddress(models.Model):
    user=models.ForeignKey(outsiders,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    contact=models.CharField(max_length=500)
    pincode=models.CharField(max_length=500)
    city=models.CharField(max_length=500)
    state=models.CharField(max_length=500)
    area=models.CharField(max_length=500)
    buildingName=models.CharField(max_length=500)
    landmark=models.CharField(max_length=500,null=True,default='No value',blank=True)
    addressType=models.CharField(max_length=500)
    orderAddressStatus=models.CharField(max_length=10)


class chat(models.Model):
    user = models.ForeignKey(outsiders, on_delete=models.CASCADE)
    uname=models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    reply = models.CharField(max_length=500,default="no reply")
    chatstatus = models.CharField(max_length=20)
    def __str__(self):
        return self.user


