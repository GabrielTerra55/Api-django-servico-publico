from rest_framework import serializers
from public_service import models

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pessoa
        fields = '__all__'
