from django.db import models

from Pet_Station.models import PetData,Food

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
    item=models.ForeignKey(PetData,on_delete=models.CASCADE,null=True,blank=True)
    fooditem=models.ForeignKey(Food,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(outsiders,on_delete=models.CASCADE)
    itemname=models.CharField(max_length=500)
    breedname=models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    quantity = models.CharField(max_length=500)
    total_price=models.CharField(max_length=500)
    category = models.CharField(max_length=10)
    expday = models.CharField(max_length=100,default='10')
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

class Favorite(models.Model):
    item=models.ForeignKey(PetData,on_delete=models.CASCADE,null=True,blank=True)
    fooditem=models.ForeignKey(Food,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(outsiders,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=500)
    image=models.ImageField(upload_to='images')
    breed=models.CharField(max_length=500)
    price=models.CharField(max_length=300)
    favStatus=models.CharField(max_length=200)
    def __str__(self):
        return self.item_name

class Order(models.Model):
    user = models.ForeignKey(outsiders, on_delete=models.CASCADE)
    fooditem=models.ForeignKey(Food,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(PetData, on_delete=models.CASCADE,null=True,blank=True)
    orderAddress =  models.ForeignKey(OrderAddress, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=500,blank=True, null=True)
    orderdate = models.CharField(max_length=100)
    breed = models.CharField(max_length=500,blank=True, null=True)
    quantity = models.CharField(max_length=500,blank=True, null=True)
    total_price = models.FloatField()
    image = models.ImageField(upload_to='images',blank=True, null=True)
    category = models.CharField(max_length=500,blank=True, null=True)
    expday = models.CharField(max_length=100,default='10')
    order_status = models.CharField(max_length=500,blank=True, null=True)

class payment(models.Model):
    user = models.ForeignKey(outsiders, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)
    def __str__(self):
        return self.amount
    


