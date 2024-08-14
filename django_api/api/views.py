from django.shortcuts import render
from rest_framework import generics, status
from .models import Product
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProductSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        Product.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # search for the primary key (id)
    lookup_field = "pk"


# create a route to get only the active products
class ProductListActive(APIView):
    def get(self, request, format=None):
        

        products_active = Product.objects.filter(active= True)

        serializer = ProductSerializer(products_active, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)


