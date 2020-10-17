from rest_framework import serializers
from .models import SystemParametrs


class SystemParametrsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SystemParametrs
        fields = ['user', 'cpu']

    user = serializers.CharField(max_length=20)
    cpu = serializers.IntegerField()

    def create(self, validated_date):
        return SystemParametrs.objects.create(**validated_date)
