from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Log
        fields = ('id', 'title', 'description', 'body', 'created', 'image', 'author_id')

    ''' title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    created = serializers.DateTimeField()
    image = serializers.ImageField()

    def create(self, validated_data):
        return Log.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.image = validated_data.get('image', instance.image)
        instance.author_id = validated_data.get('author', instance.author_id)

        instance.save()
        return instance '''