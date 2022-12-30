from rest_framework.response import Response

from blog.comments.models import Comment
from blog.tags.serializers import TagSerializer


class TagRepository(object):
    def __init__(self):
        print("TagRepository 객체 생성")

    def get_all(self):
        return Response(TagSerializer(Comment.objects.all(), many=True).data)

    def find_by_id(self):
        return Response(TagSerializer(Comment.objects.all(), many=True).data)