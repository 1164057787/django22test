from rest_framework.serializers import ModelSerializer
from app01.models import Book


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"