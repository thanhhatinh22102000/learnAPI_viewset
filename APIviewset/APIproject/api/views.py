from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Staff
from .serializers import StaffSerializer
# Create your views here.

@api_view(['GET','POST'])
def Staff_List(request):
    if request.method=='GET':
        staff=Staff.objects.all()
        serializer=StaffSerializer(staff,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Staff_Detail(request,pk):
    try:
        staff=Staff.objects.get(pk=pk)
    except Staff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=StaffSerializer(staff)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=StaffSerializer(staff,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

