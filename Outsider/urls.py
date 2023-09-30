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
    path("foodtocart",views.AddtoCartFoodAPIView.as_view(),name="foodtocart"),


    ######## view cart item in a perticular user ############
    path("singlecartitem/<int:id>",views.SingleCartAPIView.as_view(),name="singlecartitem"),
    path("cartincrementqnty/<int:id>",views.CartIncrementQuantityAPIView.as_view(),name="cartincrementqnty"),
    path("cartdecrementqnty/<int:id>",views.CartDecrementQuantityAPIView.as_view(),name="cartdecrementqnty"),
    path("deleteCartItem/<int:id>",views.Delete_CartAPIView.as_view(),name="deleteCartItem"),

    path("viewuserProfile/<int:id>",views.ProfileViewAPIView.as_view(),name="viewuserProfile"),
    path("updateuserProfile/<int:id>",views.SingleUserUpdateProfileSerializerAPIView.as_view(),name="updateuserProfile"),

    path("orderAddressSave/<int:id>",views.SaveOrderAddressAPIView.as_view(),name="orderAddressSave"),
    path("viewOrderAddress/<int:id>",views.ViewOrderAddressAPIView.as_view(),name="viewOrderAddress"),
    path("viewSingleOrderAddress/<int:id>",views.ViewSingleOrderAddressAPIView.as_view(),name="viewSingleOrderAddress"),
    path("updateOrderAddress/<int:id>",views.UpdateOrderAddressSerializerAPIView.as_view(),name="updateOrderAddress"),

    path("allOrderPrice/<int:id>",views.TotalorderPriceAPIView.as_view(),name="allOrderPrice"),

    path("favoriteItem",views.FavoriteItemAPIView.as_view(),name="favoriteItem"),
    path("favoriteFoodItem",views.FavoriteFoodItemAPIView.as_view(),name="favoriteFoodItem"),
    path("viewFavoriteItem/<int:id>",views.ViewFavoriteItemsAPIView.as_view(),name="viewFavoriteItem"),
    path("deleteFavoriteItem/<int:id>",views.Delete_FavoriteItemAPIView.as_view(),name="deleteFavoriteItem"),

    path("deleteFavoriteItemInHomePage/<int:itemId>",views.Delete_FavoriteItemInHomePageAPIView.as_view(),name=""),

    path("placeOrder",views.PlaceOrderAPIView.as_view(),name="placeOrder"),

    path("chat",views.ChatSerializerAPIview.as_view(),name="chat"),
    path("viewChat/<int:id>",views.ViewChatAPIView.as_view(),name="viewChat"),

    # path("payment",views.PaymentSerializerAPIView.as_view(),name="payment"),

    path("ratingpet/<int:id>",views.RatingPetAPIView.as_view(),name="ratingpet"),

    path("foodsView/<int:id>",views.ViewFoodsAPIView.as_view(),name="foodView"),
    path("singleFoodData/<int:fId>",views.SingleFoodDetailsAPIView.as_view(),name="singleFoodData"),
    path("ratingfood/<int:id>",views.RatingFoodAPIView.as_view(),name="ratingfood"),

    path("viewOrders/<int:userId>",views.ViewOrdersSerializerAPIView.as_view(),name="viewOrders"),
    path("searchOrderItem/<int:userId>",views.OrderItemSearchAPIView.as_view(),name="searchOrderItem"),

    path("viewNotification/<int:id>",views.ViewNotificationAPIView.as_view(),name="viewNotification")
]