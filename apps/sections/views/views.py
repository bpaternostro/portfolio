from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from ..models.resume import Person, Post
from ..serializers import PersonSerializer, PostSerializer, PostInteractSerializer

# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = PersonSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = PostSerializer

    @action(detail=True, methods=['post',], url_path='register-reaction')
    def register_reaction(self, request, pk=None):
        post = self.get_object()
        serializer = PostInteractSerializer(data=request.data)
        if serializer.is_valid():
            if request.data["field"] == "1":
                post.like += 1
            elif request.data["field"] == "2":
                post.share += 1
            else:
                post.view += 1 
            post.save()
            return Response({'status': 'interation was register OK'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)