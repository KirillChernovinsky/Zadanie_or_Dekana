from django.urls import path
from .views import index, create_product, delete

urlpatterns= [
    path('', index, name='home'),
    path('create_product/', create_product, name='create_product'),
    path('delete/<int:id>', delete, name="delete"),
    # path('telefoni', telefoni, name="telefoni"),

]