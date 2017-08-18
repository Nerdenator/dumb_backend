from rest_framework import serializers

from .models import DumbTable


class DumbSerializer(serializers.ModelSerializer):
    class Meta:
        model = DumbTable
        fields = '__all__'
        read_only_fields = ('name_field', 'number_field1', 'number_field2', 'number_field3')