from rest_framework import serializers

from blog.b_users.models import BUser as buser


class BUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    nickname = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = buser
        fields = '__all__'

    def create(self, validated_data):
        return buser.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        buser.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass
