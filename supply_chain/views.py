# supply_chain/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Supply Chain Management System</h1>")
