from django.urls import path
from . import views

urlpatterns = [
    path(
        "products/", 
         views.ProductListCreate.as_view(), 
         name="product-view-create"
         ),
    path(
        "products/<int:pk>/", 
         views.ProductRetrieveUpdateDestroy.as_view(), 
         name = "product-retrieve-update-destroy"
         ),
    path(
        "products/get-active",
        views.ProductListActive.as_view(),
        name = "product-view-active"
    )
]

