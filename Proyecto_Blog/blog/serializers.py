from rest_framework.serializers import ModelSerializer
from .models import Post

class PostListInicioSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'