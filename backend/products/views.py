# Django
from django.shortcuts import get_object_or_404

# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

# Local
from .serializers import ProcuctSerializer
from .models import Product


# This is a way to do it with class based views


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProcuctSerializer

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "content handeled by the serializer"
        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProcuctSerializer


# TODO: Add update and delete views


############### CONSTANTS FROM url.py ######################################################################
product_list_create_api_view = ProductListCreateAPIView.as_view()
product_detail_api_view = ProductDetailAPIView.as_view()
############################################################################################################


# This is a way to do it with function based views


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # Then its a single get request
            obj = get_object_or_404(Product, pk=pk)
            data = ProcuctSerializer(obj, many=False).data
            return Response(data)
        else:
            # Then its a list get request
            queryset = Product.objects.all()
            data = ProcuctSerializer(queryset, many=True).data
            return Response(data)

    if method == "POST":
        serializer = ProcuctSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            content = serializer.validated_data.get("content") or None
        if content is None:
            content = "content handeled by the serializer"
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({}, status=400)
