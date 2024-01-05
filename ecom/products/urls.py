from django.urls import path
from . import views
urlpatterns = [
    path('<slug>' , views.get_products , name="getproduct" ),
]