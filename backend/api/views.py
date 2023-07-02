from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProcuctSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    product_serializer = ProcuctSerializer(data=request.data)
    if product_serializer.is_valid(raise_exception=True):
        return Response(product_serializer.data)
    else:
        return Response({}, status=400)
