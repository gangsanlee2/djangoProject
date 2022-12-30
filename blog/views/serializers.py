from rest_framework import serializers
from blog.comments.models import Comment
from blog.views.models import View


class ViewSerializer(serializers.ModelSerializer):
    ip_address = serializers.CharField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = View
        fields = '__all__'

    def create(self, validated_data):
        return View.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        View.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
