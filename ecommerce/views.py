from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import ItemSerializer, OrderSerializer
from .models import Item , Order
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated  # I expect token to be sent via a request in the header
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin



class ItemViewSet(
        ListModelMixin,  # /list endpoint. It has def list predefined
        RetrieveModelMixin, # /get/:id endpoint
        viewsets.GenericViewSet  # list, retrieve, create, update, partial_update, destroy, 
        ):
    """
    A simple ViewSet for listing or retrieving items.
    """
    permission_classes = (IsAuthenticated,)  # Only authenticated user can access/use the endpoints
    queryset = Item.objects.all()  # Mandatory fields in all ViewSets
    serializer_class = ItemSerializer




class OrderViewSet(
        ListModelMixin,
        RetrieveModelMixin,
        UpdateModelMixin,  # Update model instance, contains def update
        viewsets.GenericViewSet
        ):
    """
    A simple ViewSet for listing, retrieving and creating orders.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        This view should return a list of all the orders
        for the currently authenticated user.
        """
        user = self.request.user
        return Order.objects.filter(user = user)

    def create(self, request):
        try:
            data = JSONParser().parse(request)  # Gets data from creation form
            serializer = OrderSerializer(data=data)
            if serializer.is_valid(raise_exception=True):  # Serializer is valid only if the validation in the serializer is True/ if check_stock is True
                item = Item.objects.get(pk = data["item"])
                order = item.place_order(request.user, data["quantity"])
                return Response(OrderSerializer(order).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)