
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate

from django.shortcuts import render,redirect

from .import models
from .models import Categories,PetData
from Outsider.models import outsiders

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
    return render(request,'chat.html')

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
        Petdata=models.PetData(categoryId=cat,categoryName=categoryName,name=name,breed=breed,age=age,gender=gender,price=price,description=description,rating=rating,image1=image1,image2=image2,image3=image3,image4=image4,petstatus=petstatus)
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
        data.rating=request.POST['rating']
        data.image1=request.POST['image1']
        data.image2=request.POST['image2']
        data.image3=request.POST['image3']
        data.image4=request.POST['image4']
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

###########    