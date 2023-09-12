from django.urls import path
from main.views import show_stock

app_name = 'main'

urlpatterns = [
    path('', show_stock, name='show_stock'),
]