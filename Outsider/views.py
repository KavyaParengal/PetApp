from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import status
from Outsider.models import Cart, Favorite, Log, Order, chat,outsiders,OrderAddress
from rest_framework.response import Response
from Outsider.serializers import UserRegisterSerializer,LoginUserSerializer,ViewCategorySerializer,ViewPetsSerializer,AddtoCartSerializer,OrderAddressSerializer,ChatSerializer,FavoriteItemSerializer,PlaceOrderSerializer,PaymentSerializer,ViewFoodsSerializer
from Pet_Station.models import Categories, Food, Notifications, PetData
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
    
class ViewFoodsAPIView(GenericAPIView):
    serializer_class=ViewFoodsSerializer
    def get(self,request,id):
        queryset=Categories.objects.all().filter(pk=id).values()
        for i in queryset:
            c_id=i['id']
            print(c_id)
        data = Food.objects.filter(categoryId=c_id).values()
        serializer_data=list(data)
        print(serializer_data)
        for obj in serializer_data:
            obj['image1']=settings.MEDIA_URL + str(obj['image1'])
            obj['image2']=settings.MEDIA_URL + str(obj['image2'])
            obj['image3']=settings.MEDIA_URL + str(obj['image3'])
            obj['image4']=settings.MEDIA_URL + str(obj['image4'])
            obj['image5']=settings.MEDIA_URL + str(obj['image5'])
        return Response({'data':serializer_data,'message':'Single Category data','success':True},status=status.HTTP_200_OK)


class SinglePetDetailsAPIView(GenericAPIView):
    def get(self,request,id):
        queryset=PetData.objects.get(pk=id)
        serializer=ViewPetsSerializer(queryset)
        return Response({'data':serializer.data,'message':'Single Pet data','success':True},status=status.HTTP_200_OK)
    

class SingleFoodDetailsAPIView(GenericAPIView):
    def get(self,request,fId):
        queryset=Food.objects.get(pk=fId)
        serializer=ViewFoodsSerializer(queryset)
        return Response({'data':serializer.data,'message':'Single Food data','success':True},status=status.HTTP_200_OK)    


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
                expday=i['expdate']
                print(ctgry)
                price=int(prices)
                print(price)
                total_price=price*quantity
                print(total_price)
                tp=str(total_price)

            producto = PetData.objects.get(id=item)
            product_image = producto.image1
            print(image)
                

            serializer = self.serializer_class(data= {'user':user,'item':item,'quantity':quantity,'total_price':tp,'cart_status':cart_status,'category':ctgry,'image':product_image,'itemname':name,'breedname':breed,'expday':expday})
            print(serializer)
            if serializer.is_valid():
                print("hi")
                serializer.save()
                return Response({'data':serializer.data,'message':'Item added to cartsuccessfully', 'success':True}, status = status.HTTP_201_CREATED)
            return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)


class AddtoCartFoodAPIView(GenericAPIView):
    serializer_class=AddtoCartSerializer
    def post(self, request):
        total_price=""
        image=""
        category=""
        food_status=""
        prices=""
        
        user = request.data.get('user')
        item=request.data.get('item')
        print(item)
        quty = request.data.get('quantity')
        quantity=int(quty)
        cart_status="0"
        
        carts = Cart.objects.filter(user=user, fooditem=item)
        if carts.exists():
            return Response({'message':'Item is already in cart','success':False}, status=status.HTTP_400_BAD_REQUEST)

        else:
            data=Food.objects.all().filter(id=item).values()
            for i in data:
                print(i)
                prices=i['price']
                print(type(prices))
                food_status=i['foodstatus']
                ctgry=i['categoryName']
                name=i['product_name']
                companyName=i['company_name']
                expday=i['expdate']
                price=float(prices)
                total_price=price*quantity
                print(total_price)
                tp=str(total_price)
    
            producto = Food.objects.get(id=item)
            product_image = producto.image1
            print(producto.image1)

            serializer = self.serializer_class(data= {'user':user,'fooditem':item,'quantity':quantity,'total_price':tp,'cart_status':cart_status,'category':ctgry,'image':product_image,'itemname':name,'breedname':companyName,'expday':expday})
            print(serializer)
            if serializer.is_valid():
                print("hi")
                serializer.save()
                return Response({'data':serializer.data,'message':'Item added to cart successfully', 'success':True}, status = status.HTTP_201_CREATED)
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

        user_id = outsiders.objects.get(id=user)
        user_id.userstatus = "1"
        user_id.save()

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
        carts=Cart.objects.filter(user=id,cart_status=0)
        print(carts)
        tot=carts.aggregate(total=Sum('total_price'))['total']
        Total_prices=str(tot)
        print(tot)
        return Response({'data':{'total_price':Total_prices},'message':'get order price successfully','success':True},status=status.HTTP_201_CREATED)


class ViewOrderAddressAPIView(GenericAPIView):
    def get(self,request,id):
        queryset=OrderAddress.objects.all().filter(user=id).values()
        serializer_data=list(queryset)
        return Response({'data':serializer_data,'message':'all Order Address','success':True},status=status.HTTP_200_OK)


# class PlaceOrderAPIView(GenericAPIView):
#     serializer_class=PlaceOrderSerializer
#     def post(self,request):
#         user=request.data.get('user')
#         date=request.data.get('date')
#         carts=Cart.objects.filter(user=user,cart_status=0)
#         if not carts.exists():
#             return Response({'message':'No item in cart to place order','success':False},status=status.HTTP_400_BAD_REQUEST)

#         order_data=[]
#         for i in carts:
#             order_data.append({
#                 'user' : user,
#                 'product' : i.item_id,
#                 'fooditem' : i.fooditem_id,
#                 'product_name' : i.itemname,
#                 'breed' : i.breedname ,
#                 'total_price' : i.total_price,
#                 'expday' : i.expday,
#                 'quantity' : i.quantity,
#                 'image' : i.image,
#                 'category' : i.category,
#                 'orderdate' : date,
#                 'order_status' : "0",
#             })
#             print("order data ========== ",order_data)
#             #i.cart_status="1"
#             i.save()
#         carts.delete()
#         serializer = self.serializer_class(data= order_data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data':serializer.data,'message':'Order placed successfully','success':True}, status = status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors,'message':'Invalid','success':False},status=status.HTTP_400_BAD_REQUEST)


class PlaceOrderAPIView(GenericAPIView):
    serializer_class = PlaceOrderSerializer
    serializer_class_payment = PaymentSerializer

    def post(self, request):
        order_id = ''
        user = request.data.get('user')
        date = request.data.get('date')
        payment_status = "0"
        carts = Cart.objects.filter(user=user)

        if not carts.exists():
            return Response({'message': 'No item in cart to place order', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

        order_data = []
        for cart in carts:  # Iterate through the Cart objects
            itemName = cart.itemname  # Access properties using dot notation
            amount = cart.total_price

            order_data.append({
                'user': user,
                'product': cart.item_id,
                'fooditem': cart.fooditem_id,
                'product_name': cart.itemname,
                'breed': cart.breedname,
                'total_price': cart.total_price,
                'expday': cart.expday,
                'quantity': cart.quantity,
                'image': cart.image,
                'category': cart.category,
                'orderdate': date,
                'order_status': "0",
            })

            cart.cart_status = "1"
            cart.save()

        carts.delete()
        serializer = self.serializer_class(data=order_data, many=True)

        if serializer.is_valid():
            order = serializer.save()
            print(order)
            for i in order:
                order_id = i.id
                print(order_id)

        serializer_order = self.serializer_class_payment(data={
            'order': order_id,
            'user': user,
            'name': itemName,
            'amount': amount,
            'date': date,
            'payment_status': payment_status
        })

        if serializer_order.is_valid():
            serializer_order.save()
            return Response({'data': serializer_order.data, 'message': 'Order placed successfully', 'success': True},
                            status=status.HTTP_201_CREATED)

        return Response({'data': serializer_order.errors, 'message': 'Invalid', 'success': False},
                        status=status.HTTP_400_BAD_REQUEST)



# class PaymentSerializerAPIView(GenericAPIView):
#     serializer_class=PaymentSerializer
#     def post(self,request):
#         user=request.data.get('user')
#         date=request.data.get('date')
#         amount=request.data.get('amount')
#         payment_status="0"
#         data=outsiders.objects.all().filter(id=user).values()
#         for i in data:
#             name=i['fullnameController']
#         serializer=self.serializer_class(data={'user':user,'date':date,'amount':amount,'payment_status':payment_status,'name':name})
#         print(serializer)
#         if serializer.is_valid():
#             print('hai')
#             serializer.save()
#             return Response({'data':serializer.data,'message':'Your payment done  Successfully','success':True},status = status.HTTP_201_CREATED)
#         return Response({'data':serializer.errors,'message':'Failed','success':False},status = status.HTTP_400_BAD_REQUEST)


class RatingPetAPIView(GenericAPIView):
    def put(self, request, id):
        try:
            ratings = PetData.objects.get(pk=id)
        except PetData.DoesNotExist:
            return Response({'message': 'Pet not found', 'success': False}, status=status.HTTP_404_NOT_FOUND)

        rate = request.data.get('rate')
        try:
            rate = float(rate)
        except ValueError:
            return Response({'message': 'Invalid rate format', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

        count = ratings.rating_count or 0 
        count += 1  
        ratings.rating_count = count

        print("Count =", count)

        if ratings.rating is None:
            ratings.rating = 0.0
        ratings.rating = (rate + ratings.rating * (count - 1)) / count
        ratings.save()

        serialized_data = ViewPetsSerializer(ratings, context={'request': request}).data
        base_url = request.build_absolute_uri('/')[:-1]
        serialized_data['image1'] = str(serialized_data['image1']).replace(base_url, '')
        serialized_data['image2'] = str(serialized_data['image2']).replace(base_url, '')
        serialized_data['image3'] = str(serialized_data['image3']).replace(base_url, '')
        serialized_data['image4'] = str(serialized_data['image4']).replace(base_url, '')

        return Response({'data': serialized_data, 'message': 'Thank you for your rating', 'success': True}, status=status.HTTP_200_OK)



class RatingFoodAPIView(GenericAPIView):
    def put(self, request, id):
        try:
            ratings = Food.objects.get(pk=id)
        except Food.DoesNotExist:
            return Response({'message': 'Food not found', 'success': False}, status=status.HTTP_404_NOT_FOUND)

        rate = request.data.get('rate')
        try:
            rate = float(rate)
        except ValueError:
            return Response({'message': 'Invalid rate format', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

        count = ratings.rating_count or 0 
        count += 1 
        ratings.rating_count = count 

        print("Count =", count)
        if ratings.rating is None:
            ratings.rating = 0.0
        ratings.rating = (rate + ratings.rating * (count - 1)) / count
        ratings.save()

        serialized_data = ViewFoodsSerializer(ratings, context={'request': request}).data
        base_url = request.build_absolute_uri('/')[:-1]
        serialized_data['image1'] = str(serialized_data['image1']).replace(base_url, '')
        serialized_data['image2'] = str(serialized_data['image2']).replace(base_url, '')
        serialized_data['image3'] = str(serialized_data['image3']).replace(base_url, '')
        serialized_data['image4'] = str(serialized_data['image4']).replace(base_url, '')
        serialized_data['image5'] = str(serialized_data['image5']).replace(base_url, '')

        return Response({'data': serialized_data, 'message': 'Thank you for your rating', 'success': True}, status=status.HTTP_200_OK)


class ChatSerializerAPIview(GenericAPIView):
    serializer_class = ChatSerializer
    def post(self,request):
        user=request.data.get('user')
        message = request.data.get('message')
        chatstatus= "0"

        data=outsiders.objects.all().filter(id=user).values()
        for i in data:
            uname=i["fullnameController"]

        serializer = self.serializer_class(data={'user':user,'uname':uname,'message':message,'chatstatus':chatstatus})
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data,'message':'You Message is sended successfully','success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)

class ViewChatAPIView(GenericAPIView):
    def get(self,request,id):
        queryset=chat.objects.all().filter(user=id).values()
        serializer_data=list(queryset)
        return Response({'data':serializer_data,'message':'all Chat details','success':True},status=status.HTTP_200_OK)


class ViewSingleOrderAddressAPIView(GenericAPIView):
    def get(self,request,id):
        queryset=OrderAddress.objects.get(pk=id)
        serializer=OrderAddressSerializer(queryset)
        return Response({'data':serializer.data,'message':'Single Order Address','success':True},status=status.HTTP_200_OK)
    
class UpdateOrderAddressSerializerAPIView(GenericAPIView):
    serializer_class = OrderAddressSerializer
    def put(self,request,id):
        queryset=OrderAddress.objects.get(pk=id)
        print(queryset)
        serializer=OrderAddressSerializer(instance=queryset,data=request.data,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'Update data Successfully','success':True},status=status.HTTP_200_OK)
        else:
            return Response({'data':'Something went wrong','success':False},status=status.HTTP_400_BAD_REQUEST)


class ViewOrdersSerializerAPIView(GenericAPIView):
    def get(self,request,userId):
        queryset=Order.objects.all().filter(user=userId).values()
        serializer_data=list(queryset)
        for obj in serializer_data:
            obj['image'] =settings.MEDIA_URL+str(obj['image'])
        return Response({'data':serializer_data,'message':'all order details','success':True},status=status.HTTP_200_OK)
    

class OrderItemSearchAPIView(GenericAPIView):
    def post(self, request, userId):
        search=request.data.get('search')
        data=Order.objects.filter(breed=search,user=userId).values()
        serialized_data=list(data)
        print(serialized_data)
        for obj in serialized_data:
            obj['image'] =settings.MEDIA_URL+str(obj['image']) 
        return Response({'data':data,'message':'Search data','success':True},status=status.HTTP_200_OK)


class FavoriteItemAPIView(GenericAPIView):
    serializer_class=FavoriteItemSerializer
    def post(self, request):
        user = request.data.get('user')
        item=request.data.get('item')
        favStatus="1"
        carts = Favorite.objects.filter(user=user, item=item)
        if carts.exists():
            return Response({'message':'Item is already in Favorite','success':False}, status=status.HTTP_400_BAD_REQUEST)

        else:
            data=PetData.objects.all().filter(id=item).values()
            for i in data:
                prices=i['price']
                name=i['name']
                breed=i['breed']

            producto = PetData.objects.get(id=item)
            product_image = producto.image1

            serializer = self.serializer_class(data= {'user':user,'item':item,'item_name':name,'image':product_image,'breed':breed,'price':prices,'favStatus':favStatus})
            print(serializer)
            if serializer.is_valid():
                print("hi")
                serializer.save()
                return Response({'data':serializer.data,'message':'Item added to Favorite successfully', 'success':True}, status = status.HTTP_201_CREATED)
            return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)


class FavoriteFoodItemAPIView(GenericAPIView):
    serializer_class=FavoriteItemSerializer
    def post(self, request):
        user = request.data.get('user')
        item = request.data.get('item')
        favStatus="1"
        carts = Favorite.objects.filter(user=user, fooditem=item)
        if carts.exists():
            return Response({'message':'Item is already in Favorite','success':False}, status=status.HTTP_400_BAD_REQUEST)

        else:
            data=Food.objects.all().filter(id=item).values()
            for i in data:
                prices=i['price']
                name=i['product_name']
                breed=i['company_name']

            producto = Food.objects.get(id=item)
            product_image = producto.image1

            serializer = self.serializer_class(data= {'user':user,'fooditem':item,'item_name':name,'image':product_image,'breed':breed,'price':prices,'favStatus':favStatus})
            print(serializer)
            if serializer.is_valid():
                print("hi")
                serializer.save()
                return Response({'data':serializer.data,'message':'Item added to Favorite successfully', 'success':True}, status = status.HTTP_201_CREATED)
            return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)



class ViewFavoriteItemsAPIView(GenericAPIView):
    def get(self, request, id):

        u_id=""
        qset =outsiders.objects.all().filter(pk=id).values()
        for i in qset:
            u_id=i['id']
            
        data = Favorite.objects.filter(user=u_id).values()
        serialized_data=list(data)
        print(serialized_data)
        for obj in serialized_data:
            obj['image'] =settings.MEDIA_URL+str(obj['image'])   
        return Response({'data' : serialized_data, 'message':'single product data','success':True},status=status.HTTP_200_OK)  


class Delete_FavoriteItemAPIView(GenericAPIView):
    def delete(self, request, id):
        delmember = Favorite.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Fav Item deleted successfully','success':True}, status = status.HTTP_200_OK)
    
from django.db.models import Q

class Delete_FavoriteItemInHomePageAPIView(GenericAPIView):
    def delete(self, request, itemId):
        # Use Q objects to create an OR condition
        delmember = Favorite.objects.filter(Q(item=itemId) | Q(fooditem=itemId)).first()

        if delmember:
            delmember.delete()
            return Response({'message': 'Fav Item deleted successfully', 'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Favorite item not found', 'success': False}, status=status.HTTP_404_NOT_FOUND)


class ViewNotificationAPIView(GenericAPIView):
    def get(self,request,id):
        queryset=Notifications.objects.all().filter(user=id).values()
        serializer_data=list(queryset)
        return Response({'data':serializer_data,'message':'all notifications','success':True},status=status.HTTP_200_OK)
