
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Note

# urls route
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'notes':'/notes/',
		'note':'/note/<str:pk>/',
		'Create':'/add/',
		'Update':'/update/<str:pk>/',
		'Delete':'/delete/<str:pk>/'
		}

	return Response(api_urls)

# get all or by id route
@api_view(['GET',"POST","DELETE","PATCH"])
def notes(request,pk=-1):
    if request.method == "GET":
        try:
            notes = Note.objects.get(id=pk)
            serializer = TaskSerializer(notes, many=False)
            return Response(serializer.data)
        except:
            notes = Note.objects.all().order_by('-id')
            serializer = TaskSerializer(notes, many=True)
            return Response(serializer.data)

    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            print("after")
            serializer.save()
        return Response(serializer.data)
        
    if request.method == "PATCH":
        note = Note.objects.get(id=pk)
        serializer = TaskSerializer(instance=note, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == "DELETE":
        note = Note.objects.get(id=pk)
        note.delete()
        return Response('Item succsesfully delete!')


        
# # add route
# @api_view(['POST'])
# def add(request):
#     serializer = TaskSerializer(data=request.data)
#     print(request.data)
#     if serializer.is_valid():
#         print("after")
#         serializer.save()
#     return Response(serializer.data)



# # update route
# @api_view(['PUT'])
# def update(request, pk):
#     note = Note.objects.get(id=pk)
#     serializer = TaskSerializer(instance=note, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# # delete route
# @api_view(['DELETE'])
# def delete(request, pk):
# 	note = Note.objects.get(id=pk)
# 	note.delete()
# 	return Response('Item succsesfully delete!')
