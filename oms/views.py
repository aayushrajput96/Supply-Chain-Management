# oms/views.py
from rest_framework.viewsets import ModelViewSet
from .models import Customer, Product, Order
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
