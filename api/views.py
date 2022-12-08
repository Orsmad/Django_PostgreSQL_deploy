
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
		'note':'/note/<str:pk>/',
		'help': 'GET,POST,DELETE,PUT'
		}

	return Response(api_urls)

# main route all methods
@api_view(['GET',"POST","DELETE","PUT"])
def notes(request,pk=-1):
    # get all or by id route
    if request.method == "GET":
        try:
            notes = Note.objects.get(id=pk)
            serializer = TaskSerializer(notes, many=False)
            return Response(serializer.data)
        except:
            notes = Note.objects.all().order_by('-id')
            serializer = TaskSerializer(notes, many=True)
            return Response(serializer.data)
    # post method
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    # update obj by id
    if request.method == "PUT":
        note = Note.objects.get(id=pk)
        serializer = TaskSerializer(instance=note, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    # delete obj by id

    if request.method == "DELETE":
        try:
            note = Note.objects.get(id=pk)
            note.delete()
        except:
            return Response('Item was not found!')
        return Response('Item succsesfully delete!')

