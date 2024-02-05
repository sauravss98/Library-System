from django.urls import path
from .apis import CartItemList, AddToCartView

urlpatterns = [ 
        path('cart-list/',CartItemList.as_view() ),
        path('cart-item/create', AddToCartView.as_view()),
        # path('login', ),
        # path('test_token', ),
]