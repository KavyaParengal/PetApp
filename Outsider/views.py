from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import status
from Outsider.models import Cart, Log,outsiders
from rest_framework.response import Response
from Outsider.serializers import UserRegisterSerializer,LoginUserSerializer,ViewCategorySerializer,ViewPetsSerializer,AddtoCartSerializer,OrderAddressSerializer
from Pet_Station.models import Categories, PetData
from django.conf import settings
from django.db.models import Sum

from rest_framework import generics
from rest_framework import filters

# Create your views here.

class UserRegisterSerializersAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    serializer_class_login = LoginUserSerializer

    def post(self, request):
        
        login_id=''
        fullnameController=request.data.get('fullnameController')
        phoneController=request.data.get('phoneController')
        emailController=request.data.get('emailController')
        usernmController=request.data.get('usernmController')
        pwdController=request.data.get('pwdController')
        role='user'
        userstatus='0'

        if(Log.objects.filter(usernmController=usernmController)):
            return Response({'message': 'Duplicate User Found'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login = self.serializer_class_login(data = {'usernmController':usernmController,'pwdController':pwdController,'role':role})

        if serializer_login.is_valid():
            log = serializer_login.save()
            login_id = log.id
            print(login_id)
        serializer = self.serializer_class(data= {'log_id':login_id,'fullnameController':fullnameController,'phoneController':phoneController,'emailController':emailController,'usernmController':usernmController,'pwdController':pwdController,'role':role,'userstatus':userstatus})
        print(serializer)
        if serializer.is_valid():
            print('hai')
            serializer.save()
            return Response({'data':serializer.data,'message':'User registered successfully','success':True},status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'Failed Your Registration','success':False},status = status.HTTP_400_BAD_REQUEST)
    

class LoginUserAPIView(GenericAPIView):
    serializer_class = LoginUserSerializer
    def post(self,request):
        usernmController=request.data.get('usernmController')
        pwdController=request.data.get('pwdController')
        logreg=Log.objects.filter(usernmController=usernmController,pwdController=pwdController)
        if(logreg.count()>0):
            read_serializer=LoginUserSerializer(logreg, many=True)
            for i in read_serializer.data:
                id=i['id']
                print(id)
                role=i['role']
                regdata=outsiders.objects.all().filter(log_id=id).values()
                print(regdata)
                for i in regdata:
                    u_id=i['id']
                    l_status=i['userstatus']
                    f_name=i['fullnameController']
                    print(u_id)

            return Response({'data':{'login_id':id,'usernmController':usernmController,'pwdController':pwdController,'role':role,'user_id':u_id,'l_status':l_status,'name':f_name},'success':True,'message':'Logged in successfully'},status = status.HTTP_201_CREATED)
        else:
            return Response({'data':'username or password is invalid','message':'Username or Password is Invalid','success':False,},status = status.HTTP_400_BAD_REQUEST)

########## view Category ####################

class ViewCategoryAPIView(GenericAPIView):
    serializer_class=ViewCategorySerializer
    def get(self,request):
        queryset=Categories.objects.all()
        if(queryset.count()>0):
            serializer=ViewCategorySerializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'all Categories','success':True},status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available','success':False},status=status.HTTP_400_BAD_REQUEST)
        
class ViewPetInSingleCategoryAPIView(GenericAPIView):
    serializer_class=ViewPetsSerializer
    def get(self,request,id):
        queryset=Categories.objects.all().filter(pk=id).values()
        for i in queryset:
            c_id=i['id']
            print(c_id)
        data = PetData.objects.filter(categoryId=c_id).values()
        serializer_data=list(data)
        print(serializer_data)
        for obj in serializer_data:
            obj['image1']=settings.MEDIA_URL + str(obj['image1'])
            obj['image2']=settings.MEDIA_URL + str(obj['image2'])
            obj['image3']=settings.MEDIA_URL + str(obj['image3'])
            obj['image4']=settings.MEDIA_URL + str(obj['image4'])
        return Response({'data':serializer_data,'message':'Single Category data','success':True},status=status.HTTP_200_OK)

class SinglePetDetailsAPIView(GenericAPIView):
    def get(self,request,id):
        queryset=PetData.objects.get(pk=id)
        serializer=ViewPetsSerializer(queryset)
        return Response({'data':serializer.data,'message':'Single Pet data','success':True},status=status.HTTP_200_OK)


class ViewAllCategoryItemAPIView(GenericAPIView):
    serializer_class=ViewPetsSerializer
    def get(self,request):
        queryset=PetData.objects.all()
        if(queryset.count()>0):
            serializer=ViewPetsSerializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'all Categories Items','success':True},status=status.HTTP_200_OK)
        else:
            return Response({'data':'No data available','success':False},status=status.HTTP_400_BAD_REQUEST)
        

class AddtoCartAPIView(GenericAPIView):
    serializer_class=AddtoCartSerializer
    def post(self, request):
        total_price=""
        image=""
        category=""
        p_status=""
        prices=""
        
        user = request.data.get('user')
        item=request.data.get('item')
        print(item)
        quty = request.data.get('quantity')
        quantity=int(quty)
        cart_status="0"
        
        carts = Cart.objects.filter(user=user, item=item)
        if carts.exists():
            return Response({'message':'Item is already in cart','success':False}, status=status.HTTP_400_BAD_REQUEST)

        else:
            data=PetData.objects.all().filter(id=item).values()
            for i in data:
                print(i)
                prices=i['price']
                p_status=i['petstatus']
                ctgry=i['categoryName']
                name=i['name']
                breed=i['breed']
                print(ctgry)
                price=int(prices)
                print(price)
                total_price=price*quantity
                print(total_price)
                tp=str(total_price)

            producto = PetData.objects.get(id=item)
            product_image = producto.image1
            print(image)
                

            serializer = self.serializer_class(data= {'user':user,'item':item,'quantity':quantity,'total_price':tp,'cart_status':cart_status,'category':ctgry,'image':product_image,'itemname':name,'breedname':breed})
            print(serializer)
            if serializer.is_valid():
                print("hi")
                serializer.save()
                return Response({'data':serializer.data,'message':'Item added to cartsuccessfully', 'success':True}, status = status.HTTP_201_CREATED)
            return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)


class SingleCartAPIView(GenericAPIView):
    def get(self, request, id):

        u_id=""
        qset =outsiders.objects.all().filter(pk=id).values()
        for i in qset:
            u_id=i['id']


        data = Cart.objects.filter(user=u_id).values()
        serialized_data=list(data)
        print(serialized_data)
        for obj in serialized_data:
            obj['image'] =settings.MEDIA_URL+str(obj['image'])   
        return Response({'data' : serialized_data, 'message':'single product data','success':True},status=status.HTTP_200_OK)  



class CartIncrementQuantityAPIView(GenericAPIView):
    def put(self, request, id):
        cart_item = Cart.objects.get(pk=id)


        qnty=cart_item.quantity
        qty=int(qnty)

        cart_item.quantity=qty + 1

        q=cart_item.quantity
        qn=int(q)

        pr=cart_item.item.price
        price=int(pr)


        tp=price*qn
        cart_item.total_price=tp


        cart_item.save()
        serialized_data = AddtoCartSerializer(cart_item,context={'request':request}).data
        # serialized_data['image']=str(serialized_data['image']).split('http://localhost:8000')[1]
        base_url=request.build_absolute_uri('/')[:-1]
        serialized_data['image']=str(serialized_data['image']).replace(base_url,'')
        return Response({'data' : serialized_data, 'message':'cart item quantity updated','success':True},status=status.HTTP_200_OK)  

class CartDecrementQuantityAPIView(GenericAPIView):
    def put(self, request, id):
        cart_item = Cart.objects.get(pk=id)


        qny=cart_item.quantity
        qant=int(qny)
        
        if qant > 1:
            qnty=cart_item.quantity
            qty=int(qnty)
            cart_item.quantity=qty - 1

            q=cart_item.quantity
            qn=int(q)

            pr=cart_item.item.price
            price=int(pr)


            tp=price*qn
            cart_item.total_price=tp


            cart_item.save()
            serialized_data = AddtoCartSerializer(cart_item,context={'request':request}).data
            base_url=request.build_absolute_uri('/')[:-1]
            serialized_data['image']=str(serialized_data['image']).replace(base_url,'')

            return Response({'data' : serialized_data, 'message':'cart item quantity updated','success':True},status=status.HTTP_200_OK)
        else:
            return Response({'message':'Quantity cannot be less than 1','success':False},status=status.HTTP_400_BAD_REQUEST)  

class Delete_CartAPIView(GenericAPIView):
    def delete(self, request, id):
        delmember = Cart.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Cart Item deleted successfully','success':True}, status = status.HTTP_200_OK)

class ProfileViewAPIView(GenericAPIView):
    def get(self,request,id):
        queryset=outsiders.objects.get(pk=id)
        serializer=UserRegisterSerializer(queryset)
        return Response({'data':serializer.data,'message':'Single user data','success':True},status=status.HTTP_200_OK)
    
class SingleUserUpdateProfileSerializerAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def put(self,request,id):
        queryset=outsiders.objects.get(pk=id)
        print(queryset)
        serializer=UserRegisterSerializer(instance=queryset,data=request.data,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'Update data Successfully','success':True},status=status.HTTP_200_OK)
        else:
            return Response({'data':'Something went wrong','success':False},status=status.HTTP_400_BAD_REQUEST)


class ItemSearchAPIView(GenericAPIView):
    def post(self, request):
        search=request.data.get('search')
        data=PetData.objects.filter(breed=search).values()
        serialized_data=list(data)
        print(serialized_data)
        for obj in serialized_data:
            obj['image1'] =settings.MEDIA_URL+str(obj['image1']) 
            obj['image2'] =settings.MEDIA_URL+str(obj['image2']) 
            obj['image3'] =settings.MEDIA_URL+str(obj['image3']) 
            obj['image4'] =settings.MEDIA_URL+str(obj['image4']) 
        return Response({'data':data,'message':'Search data','success':True},status=status.HTTP_200_OK)


class SaveOrderAddressAPIView(GenericAPIView):
    serializer_class=OrderAddressSerializer
    def post(self,request,id):
        user=request.data.get("user")
        pincode=request.data.get("pincode")
        city=request.data.get("city")
        state=request.data.get("state")
        area=request.data.get("area")
        buildingName=request.data.get("buildingName")
        landmark=request.data.get("landmark")
        addressType=request.data.get("addressType")
        orderAddressStatus="0"
        data=outsiders.objects.all().filter(id=user).values()
        for i in data :
            name=i['fullnameController']
            print(name)
            contact=i['phoneController']
            print(contact)
        serializer=self.serializer_class(data={'user':user,'name':name,'contact':contact,'pincode':pincode,'city':city,'state':state,'area':area,'buildingName':buildingName,'landmark':landmark,'addressType':addressType,'orderAddressStatus':orderAddressStatus})
        print(serializer)
        if serializer.is_valid():
            print('hai')
            serializer.save()
            return Response({'data':serializer.data,'message':'Your address saved Successfully','success':True},status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'Failed','success':False},status = status.HTTP_400_BAD_REQUEST)
    

class TotalorderPriceAPIView(GenericAPIView):
     def get(self,request,id):
        carts=Cart.objects.filter(user=id)
        print(carts)
        tot=carts.aggregate(total=Sum('total_price'))['total']
        Total_prices=str(tot)
        print(tot)
        return Response({'data':{'total_price':Total_prices},'message':'get order price successfully','success':True},status=status.HTTP_201_CREATED)

