from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('addstock', views.add_stock, name="addstock"),
    path('deletestock/<stock_id>', views.delete_stock, name="deletestock"),  #  like this - 'deletestock/<stock_id>' because need to pass stock id 
    # to be deleted in function and url in html "{% url 'deletestock' company.ticker_id %}"
]