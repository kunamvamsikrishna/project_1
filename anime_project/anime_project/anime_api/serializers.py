from serializers import serializer
from blog.models import * 


class AnimeSerializer(serializer.ModelSerializer):
     class Meta:
          model = Anime
          fields = '__all__'