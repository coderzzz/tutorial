from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from gmoji.models import Gmoji
from gmoji.serializers import GmojiSerializer
# Create your views here.


# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """

#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)


# @csrf_exempt
# @api_view(['GET', 'POST'])
# def gmoji_list(request):

#     if request.method == 'GET':
#         snippets = Gmoji.objects.all()
#         serializer = GmojiSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = GmojiSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

class GmojiList(APIView):
    
    def get(self, request, format=None):

        gmojis = Gmoji.objects.all()
        serializer = GmojiSerializer(gmojis,many = True)
        print(request.query_params.dict())
        return Response(serializer.data)
    
    def post(self, request, format=None):

        serializer = GmojiSerializer(data=request.data)
        print(request.data.dict())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
