from rest_framework import serializers
from .models import Photo, Comment, Rating


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = "__all__"


# class LikedPhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LikedPhoto
#         fields = "__all__"
