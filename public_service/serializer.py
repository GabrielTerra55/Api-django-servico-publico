from rest_framework import serializers
from public_service import models
from public_service.validators import *

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pessoa
        fields = '__all__'

    def validate(self, data):
        """Validation of cpf and name"""

        if not cpf_valid(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF invalido'})

        if not name_valid(data['name']):
            raise serializers.ValidationError({'name': 'insira somente letras'})

        return data