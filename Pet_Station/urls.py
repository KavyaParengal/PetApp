from django.urls import path

from Pet_Station import views

urlpatterns=[
    
    path("",views.login_page,name="login_page"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("add_category",views.add_category,name="add_category"),
    path("edit_category",views.edit_category,name="edit_category"),
    path("view_category",views.view_category,name="view_category"),
    path("add_pet",views.add_pet,name="add_pet"),
    path("edit_pet",views.edit_pet,name="edit_pet"),
    path("view_pet",views.view_pet,name="view_pet"),
    path("add_food",views.add_food,name="add_food"),
    path("edit_food",views.edit_food,name="edit_food"),
    path("view_food",views.view_food,name="view_food"),
    path("view_user",views.view_user,name="view_user"),
    path("add_notification",views.add_notification,name="add_notification"),
    path("view_notification",views.view_notification,name="view_notification"),
    path("chatWithUser",views.chatWithUser,name="chatWithUser"),

    path("login_user",views.login_user,name="login_user"),

    ######### manage category ##############

    path("adminAddCategory",views.adminAddCategory,name="adminAddCategory"),
    path("adminviewsCategory",views.adminviewsCategory,name="adminviewsCategory"),
    path("adminEditCategory<int:categoryId>",views.adminEditCategory,name="adminEditCategory"),
    path("updateCategory<int:categoryId>",views.updateCategory,name="updateCategory"),
    path("deleteCategory<int:categoryId>",views.deleteCategory,name="deleteCategory"),

    ############## manage pets ##################

    path("addPets",views.addPets,name="addPets"),
    path("viewPets",views.viewPets,name="viewPets"),
    path("adminEditPet<int:petId>",views.adminEditPet,name="adminEditPet"),
    path("updatePet<int:petId>",views.updatePet,name="updatePet"),
    path("deletePet<int:petId>",views.deletePet,name="deletePet"),

    path("viewUsers",views.viewUsers,name="viewUsers"),

]
