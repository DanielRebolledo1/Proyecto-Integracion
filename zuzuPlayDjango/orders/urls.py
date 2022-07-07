from django.urls import path
from .views import checkout, payment, orders, detail, tracking, confirmation, confirmationEx

urlpatterns = [
    path('checkout', checkout, name="checkout"),
    path('checkout/payment', payment, name="payment"),
    path('checkout/confirmation/<idOrden>', confirmation, name="confirmation"),
    path('conf', confirmationEx, name="confirmationEx"),
    path('account/orders', orders, name="orders"),
    path('account/orders/detail/<id>', detail, name="detail"),
    path('account/orders/tracking/<id>', tracking, name="tracking"),
]
