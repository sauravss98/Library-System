from django.urls import path
from .apis import AddToCart,ViewCart,ModifyCart,Checkout

urlpatterns = [ 
        path('cart-list/',ViewCart.as_view() ),
        path('cart-item/create', AddToCart.as_view()),
        path('modify-cart/<int:cart_item_id>/<int:book_id>',ModifyCart.as_view()),
        path('checkout/',Checkout.as_view())
]