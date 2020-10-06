from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Photo, Comment, Rating
from .serializers import PhotoSerializer, CommentSerializer, RatingSerializer


# Create your views here.
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    # @action(detail=True ,methods=['post'])
    # def hello_world(self, request):
    #     return Response({"message": "Hello, world!"})


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


# def email_me(request):

    # class LikedPhotoViewSet(viewsets.ModelViewSet):
    #     queryset = LikedPhoto.objects.all()
    #     serializer_class = LikedPhotoSerializer
