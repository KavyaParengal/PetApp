
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate

from django.shortcuts import render,redirect

from .import models
from .models import Categories, Food, Notifications,PetData
from Outsider.models import Order, outsiders,chat, payment

from django.shortcuts import get_object_or_404

# Create your views here.

######## login ##############

def login_page(request):
    return render(request,'login.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user is not None:
            auth_login(request,user)
            return render(request,'dashboard.html')

        else:
            messages.info(request,'Invalid credentials')
            return redirect('login_page')

    else:
        return render(request,'login.html')
    
######### single pages ###########


def dashboard(request):
    return render(request,'dashboard.html')

def add_category(request):
    return render(request,'add_categories.html')

def edit_category(request):
    return render(request,'edit_categories.html')

def view_category(request):
    return render(request,'view_categories.html')

def add_pet(request):
    return render(request,'add_pets.html')

def edit_pet(request):
    return render(request,'edit_pets.html')

def view_pet(request):
    return render(request,'view_pets.html')

def add_food(request):
    return render(request,'add_food.html')

def edit_food(request):
    return render(request,'edit_foods.html')

def view_food(request):
    return render(request,'view_food.html')

def view_user(request):
    return render(request,'view_user.html')

def add_notification(request):
    return render(request,'add_notification.html')

def view_notification(request):
    return render(request,'view_notification.html')

def chatWithUser(request):
    return render(request,'viewchat.html')

########### add category ########################

def adminAddCategory(request):
    if request.method=='POST' and request.FILES:
        category_name=request.POST.get('category_name')
        category_image=request.FILES['category_image']
        category_status="0"

        userDetails=models.Categories(category_name=category_name,category_image=category_image,category_status=category_status)
        userDetails.save()

        print("Category Add")

        return redirect(adminviewsCategory)
    else:
        return render(request,'add_categories.html')
    
def adminviewsCategory(request):
    data=Categories.objects.all()
    return render(request,'view_categories.html',{'data':data})

def adminEditCategory(request,categoryId):
    data=Categories.objects.get(id=categoryId)
    return render(request,'edit_categories.html',{'data':data})

def updateCategory(request,categoryId):
    if request.method=='POST':
        data=Categories.objects.get(id=categoryId)
        data.category_name=request.POST['category_name']
        data.category_image=request.FILES['category_image']
        data.save()
        return redirect("adminviewsCategory")
    
def deleteCategory(request,categoryId):
    item=Categories.objects.get(id=categoryId)
    item.delete()
    messages.info(request,'delete successfully')
    return redirect('adminviewsCategory')

############## add Pets ############################

def addPets(request):
    if request.method=='POST' and request.FILES:
        categoryName=request.POST.get('cgname')
        name=request.POST.get('name')
        breed=request.POST.get('breed')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        price=request.POST.get('price')
        description=request.POST.get('description')
        expdate=request.POST.get('expdate')
        rating=request.POST.get('rating')
        image1=request.FILES['image1']
        image2=request.FILES['image2']
        image3=request.FILES['image3']
        image4=request.FILES['image4']
        petstatus='0'

        cat=Categories.objects.get(category_name=categoryName)
        # for i in cat:
        #     c_id=i['id']
        print(cat)
        Petdata=models.PetData(categoryId=cat,categoryName=categoryName,name=name,breed=breed,age=age,gender=gender,price=price,description=description,rating=rating,expdate=expdate,image1=image1,image2=image2,image3=image3,image4=image4,petstatus=petstatus)
        Petdata.save()
        return redirect('viewPets')
    else:
        return render(request,'add_pets.html')
    

def viewPets(request):
    data=PetData.objects.all()
    return render(request,'view_pets.html',{'data':data})

def adminEditPet(request,petId):
    data=PetData.objects.get(id=petId)
    return render(request,'edit_pets.html',{'data':data})

def updatePet(request,petId):
    if request.method=='POST':
        data=PetData.objects.get(id=petId)
        data.categoryName=request.POST['cgname']
        data.name=request.POST['name']
        data.breed=request.POST['breed']
        data.age=request.POST['age']
        data.gender=request.POST['gender']
        data.price=request.POST['price']
        data.description=request.POST['description']
        data.expdate=request.POST['expdate']
        data.image1=request.FILES['image1']
        data.image2=request.FILES['image2']
        data.image3=request.FILES['image3']
        data.image4=request.FILES['image4']
        data.save()
        return redirect("viewPets")
    
def deletePet(request,petId):
    item=PetData.objects.get(id=petId)
    item.delete()
    messages.info(request,'delete successfully')
    return redirect('viewPets')

########## admin view users ######################

def viewUsers(request):
    data=outsiders.objects.all()
    return render(request,'view_user.html',{'data':data})   

###########    add food ############################

def addFood(request):
    if request.method=='POST' and request.FILES:
        categoryName=request.POST.get('cgname')
        product_name=request.POST.get('product_name')
        product_type=request.POST.get('product_type')
        net_weight=request.POST.get('net_weight')
        company_name=request.POST.get('company_name')
        benefit=request.POST.get('benefit')
        price=request.POST.get('price')
        marketed_by=request.POST.get('marketed_by')
        description=request.POST.get('description')
        expdate=request.POST.get('expdate')
        rating=request.POST.get('rating')
        image1=request.FILES['image1']
        image2=request.FILES['image2']
        image3=request.FILES['image3']
        image4=request.FILES['image4']
        image5=request.FILES['image5']
        foodstatus='0'

        cat=Categories.objects.get(category_name=categoryName)
        # for i in cat:
        #     c_id=i['id']
        print(cat)
        Petdata=models.Food(categoryId=cat,categoryName=categoryName,product_name=product_name,product_type=product_type,
                            net_weight=net_weight,company_name=company_name,benefit=benefit,price=price,marketed_by=marketed_by,
                            description=description,rating=rating,expdate=expdate,image1=image1,image2=image2,image3=image3,
                            image4=image4,image5=image5,foodstatus=foodstatus)
        Petdata.save()
        return redirect('viewFoods')
    else:
        return render(request,'add_food.html')
    
def viewFoods(request):
    data=Food.objects.all()
    return render(request,'view_food.html',{'data':data})

def adminEditFood(request,foodId):
    data=Food.objects.get(id=foodId)
    return render(request,'edit_foods.html',{'data':data})

def updateFood(request,foodId):
    if request.method=='POST':
        data=Food.objects.get(id=foodId)
        data.categoryName=request.POST['cgname']
        data.product_name=request.POST['product_name']
        data.product_type=request.POST['product_type']
        data.net_weight=request.POST['net_weight']
        data.company_name=request.POST['company_name']
        data.benefit=request.POST['benefit']
        data.price=request.POST['price']
        data.marketed_by=request.POST['marketed_by']
        data.description=request.POST['description']
        data.expdate=request.POST['expdate']
        data.image1=request.FILES['image1']
        data.image2=request.FILES['image2']
        data.image3=request.FILES['image3']
        data.image4=request.FILES['image4']
        data.image5=request.FILES['image5']
        data.save()
        return redirect("viewFoods")

def deleteFood(request,foodId):
    item=Food.objects.get(id=foodId)
    item.delete()
    messages.info(request,'delete successfully')
    return redirect('viewFoods')


########## view chat ###############

def viewChat(request):
    data=chat.objects.all()
    return render(request,'viewchat.html',{'data':data})

def replyChat(request,id):
    data=chat.objects.get(id=id)
    print(data)
    return render(request,'reply.html',{'data':data})

def updateChat(request,id):
    if request.method=='POST':
        data=chat.objects.get(id=id)
        data.reply=request.POST['reply']
        data.save()
        return redirect("viewChat")

############# view Orders #####################################

def viewOrder(request):
    data=Order.objects.all()
    return render(request,'view_orders.html',{'data':data})

def viewPayment(request):
    data=payment.objects.all()
    return render(request,'viewPayments.html',{'data':data})

############# notification add ###########################

def notificationPage(request,id):
    data=Order.objects.get(id=id)
    return render(request,'add_notification.html',{'data':data})

def addNotification(request):
    if request.method == 'POST':
        order_id = request.POST.get('order')
        notification_title = request.POST.get('notification_title')
        notification_content = request.POST.get('notification_content')
        date = request.POST.get('date')
        notification_status = "0"
        print(order_id)
        
        order = get_object_or_404(Order, id=order_id)
        print(order)

        userId = order.user_id

        user = get_object_or_404(outsiders, id=userId)

        notificationDetails = models.Notifications(
            user=user,
            order=order,
            notification_title=notification_title,
            notification_content=notification_content,
            date=date,
            notification_status=notification_status
        )
        notificationDetails.save()
        print(notificationDetails)
        
        return redirect(viewNotification)
    else:
        return render(request, 'add_notification.html')
    
def viewNotification(request):
    data=Notifications.objects.all()
    return render(request,'view_notification.html',{'data':data})
    
def deleteNotification(request,notifyId):
    item=Notifications.objects.get(id=notifyId)
    item.delete()
    messages.info(request,'delete successfully')
    return redirect('viewNotification')

