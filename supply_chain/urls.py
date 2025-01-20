# supply_chain/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Import HttpResponse
from rest_framework.routers import DefaultRouter
from oms.views import CustomerViewSet, ProductViewSet, OrderViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', lambda request: HttpResponse("<h1>Welcome to the Supply Chain Management System</h1>"), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include API endpoints
]
