from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def get_Data(request):
    """
    GET All records

    Rota referente a visualização ou requisição GET de todos os registros da base de dados.
    GET Route that shows all the records from the database.
    """
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def add_Data(request):
    """
    POST create new record

    Rota referente a criação de um novo registro na base de dados usando requisição POST.
    POST Route that creates a new record in the database.
    """
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def update_Data(request, pk):
    """
    PUT updates all fields of a record

    Rota referente a atualização de todos os campos de um registro na base de dados.
    PUT Route that updates all fields of a record in the database.
    """
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def partial_update_Data(request, pk):
    """
    PATCH updates some fields of a record

    Rota referente a atualização de alguns dos campos de um registro na base de dados.
    PATCH Route that updates some fields of a record in the database.
    """
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ItemSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_Data(request,pk):
    """
    DELETE deletes a record from the database
    
    Rota referente a deleção de um registro da base de dados.
    DELETE Route that erases a record from the database.
    """
    try:
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)