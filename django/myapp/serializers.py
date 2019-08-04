from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class ExplicitPersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 128)
    email = serializers.EmailField()
    add_date = serializers.DateTimeField()
