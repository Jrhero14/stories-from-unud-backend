from rest_framework import serializers

from DATABASE.models import BlogMainDatabase, queueArticle

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogMainDatabase
        fields = ['HashNumber', 'title', 'imageUrl', 'article', 'dateTimeCreated', 'author', 'visitor']


class queueArticleSerialize(serializers.ModelSerializer):
    class Meta:
        model = queueArticle
        fields = ['HashNumber', 'title', 'imageUrl', 'article', 'dateTimeCreated', 'author', 'visitor']