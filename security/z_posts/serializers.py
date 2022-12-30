from rest_framework import serializers

from security.z_posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    content = serializers.CharField()
    create_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Post.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
