from rest_framework import serializers

from Outsider.models import Log,outsiders,Cart,OrderAddress,chat,Favorite,Order,payment
from Pet_Station.models import Categories,PetData,Food

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = outsiders
        fields = '__all__'
        def create(self,validated_data):
            return outsiders.objects.create(**validated_data)
        
class ViewCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        def create(self,validated_data):
            return Categories.objects.create(**validated_data)
        

class ViewPetsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PetData
        fields='__all__'
        def create(self,validated_data):
            return PetData.objects.create(**validated_data)
        
class ViewFoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields='__all__'
        def create(self,validated_data):
            return Food.objects.create(**validated_data)

class AddtoCartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__' 
        def create(self,validated_data):
            return Cart.objects.create(**validated_data)    


class OrderAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderAddress
        fields='__all__' 
        def create(self,validated_data):
            return OrderAddress.objects.create(**validated_data)

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=chat
        fields='__all__' 
        def create(self,validated_data):
            return chat.objects.create(**validated_data)  

class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorite
        fields='__all__' 
        def create(self,validated_data):
            return Favorite.objects.create(**validated_data)      

class PlaceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
        def create(self,validated_data):
            return Order.objects.create(**validated_data)
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'
    def Create(self, validated_data):
        return payment.objects.Create(**validated_data)

