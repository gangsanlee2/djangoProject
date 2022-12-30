from rest_framework import serializers

from blog.tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    content = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    parent_id = serializers.CharField()

    class Meta:
        model = Tag
        fields = '__all__'

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Tag.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
