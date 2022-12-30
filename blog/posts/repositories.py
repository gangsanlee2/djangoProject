from rest_framework.response import Response

from blog.posts.models import Post
from blog.posts.serializers import PostSerializer


class PostRepository(object):
    def __init__(self):
        print("PostRepository 객체 생성")

    def get_all(self):
        return Response(PostSerializer(Post.objects.all(), many=True).data)

    def find_by_id(self):
        return Response(PostSerializer(Post.objects.all(), many=True).data)