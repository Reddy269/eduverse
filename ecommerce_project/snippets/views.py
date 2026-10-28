from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import serializers, status
from snippets.models import Snippet
from oauth2_provider.contrib.rest_framework import OAuth2Authentication

@api_view(['GET'])
@authentication_classes([OAuth2Authentication])
def get_snippet(request):

    l = []
    for snippet in Snippet.objects.all():
        obj = Snippet.objects.get(id=snippet.id)
        l.append(obj)

    responseserializer = OutputSnippetSerializer(l, many=True)
    return Response(responseserializer.data)


    #create a list that holds CreateSnippetResponse object for every instance in Snippet model
    #serialize this list with many = true
    #return Response



    return Response({'message': 'success'})


@api_view(['POST'])
def create_snippet(request):

    serializer = InputSnippetSerializer(data=request.data)
    if serializer.is_valid():
        obj1 = serializer.save()
        obj2 = register_snippet(obj1.title,obj1.code)
        snippetresponse = CreateSnippetResponse(obj2.id,obj2.code,obj2.title)
        response_serializer = OutputSnippetSerializer(snippetresponse)
        return Response(response_serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #check for errors ??




class CreateSnippetRequest:
    def __init__(self,code,title = ''):
        self.code = code
        self.title = title

class CreateSnippetResponse:
    def __init__(self,id,code,title = ''):
        self.id= id
        self.code = code
        self.title = title

class InputSnippetSerializer(serializers.Serializer):
    title = serializers.CharField(required=False , allow_blank= True ,max_length=100)
    code = serializers.CharField()

    def create(self, a):
        return CreateSnippetRequest(**a)

def register_snippet(title,code):

    return Snippet.objects.create(title=title,code=code)

class OutputSnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField()
    title = serializers.CharField(required=False , allow_blank= True ,max_length=100)

    def create(self, a):
        return CreateSnippetResponse(**a)






