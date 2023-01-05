from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

# model import
from .models import Note


"""views"""
# urls route
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'notes':'/notes/',
		'notes':'/notes/<str:pk>/',
		'help': 'GET,POST,DELETE,PUT'
		}

	return Response(api_urls)

# main route all methods
@api_view(['GET',"POST","DELETE","PUT"])
def notes(request,pk=-1):
    # get all or by id route
    if request.method == "GET":
        if pk ==-1:
            notes = Note.objects.all().order_by('-id')
            serializer = TaskSerializer(notes, many=True)
            return Response(serializer.data)
        else:
            try:
                notes = Note.objects.get(id=pk)
                serializer = TaskSerializer(notes, many=False)
                return Response(serializer.data)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
          
    # post method
    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # update obj by id
    elif request.method == "PUT":
        try:
            note = Note.objects.get(id=pk)
            serializer = TaskSerializer(instance=note, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # delede obj by id
    elif request.method == "DELETE":
        try:
            note = Note.objects.get(id=pk)
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except :
                return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

