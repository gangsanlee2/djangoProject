from django.http import JsonResponse
from rest_framework.response import Response

from blog.comments.models import Comment
from blog.comments.serializers import CommentSerializer


class CommentRepository(object):
    def __init__(self):
        print("CommentRepository 객체 생성")

    def get_all(self):
        return Response(CommentSerializer(Comment.objects.all(), many=True).data)

    def find_by_id(self):
        return Response(CommentSerializer(Comment.objects.all(), many=True).data)