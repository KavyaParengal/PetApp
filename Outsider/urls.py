from Outsider import views
from django.urls import path

urlpatterns = [
    path('login_users',views.LoginUserAPIView.as_view(),name='login_users'),
    path('user_register',views.UserRegisterSerializersAPIView.as_view(),name='user_register'),
    path("view_categories",views.ViewCategoryAPIView.as_view(),name='view_categories'),
    path("singleCategorydatas/<int:id>",views.ViewPetInSingleCategoryAPIView.as_view(),name='singleCategorydatas'),
    path("singlePetDetails/<int:id>",views.SinglePetDetailsAPIView.as_view(),name="singlePetDetails"),
    path("allpetdetails",views.ViewAllCategoryItemAPIView.as_view(),name="allpetdetails"),
    path('item-search',views.ItemSearchAPIView.as_view(), name='item-search'),
    path("addtocart",views.AddtoCartAPIView.as_view(),name="addtocart"),

    ######## view cart item in a perticular user ############
    path("singlecartitem/<int:id>",views.SingleCartAPIView.as_view(),name="singlecartitem"),
    path("cartincrementqnty/<int:id>",views.CartIncrementQuantityAPIView.as_view(),name="cartincrementqnty"),
    path("cartdecrementqnty/<int:id>",views.CartDecrementQuantityAPIView.as_view(),name="cartdecrementqnty"),
    path("deleteCartItem/<int:id>",views.Delete_CartAPIView.as_view(),name="deleteCartItem"),

    path("viewuserProfile/<int:id>",views.ProfileViewAPIView.as_view(),name="viewuserProfile"),
    path("updateuserProfile/<int:id>",views.SingleUserUpdateProfileSerializerAPIView.as_view(),name="updateuserProfile"),

    path("orderAddressSave/<int:id>",views.SaveOrderAddressAPIView.as_view(),name="orderAddressSave"),
    path("allOrderPrice/<int:id>",views.TotalorderPriceAPIView.as_view(),name="allOrderPrice"),
]