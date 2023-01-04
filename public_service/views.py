from rest_framework import viewsets
from public_service import models
from public_service import serializer

class PessoaViewset(viewsets.ModelViewSet):
    "exibindo todas as pessoas"

    queryset = models.Pessoa.objects.all()
    serializer_class = serializer.PessoaSerializer
