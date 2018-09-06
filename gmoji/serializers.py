from django.contrib.auth.models import User
from rest_framework import serializers
from gmoji.models import Gmoji


class GmojiSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Gmoji
        fields = ('id', 'created', 'image_url', 'title', 'code',
                  'config')
