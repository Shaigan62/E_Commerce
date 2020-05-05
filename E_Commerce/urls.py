
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
    path('orders/',include('orders.urls')),
    path('productsearch/',include('search_app.urls')),
    path('shoppingcart/',include('shoppingcart.urls')),
]
