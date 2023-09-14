from rest_framework import serializers

from Outsider.models import Log,outsiders,Cart,OrderAddress
from Pet_Station.models import Categories,PetData

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

class OrderAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderAddress
        fields='__all__' 
        def create(self,validated_data):
            return OrderAddress.objects.create(**validated_data)      

