from rest_framework import viewsets, request, filters
from django.http import JsonResponse
from public_service.model.schooling import dict_schooling
from public_service.model.states_of_life import dict_states_of_life
from public_service.model.status import dict_status
from public_service.model.states import dict_states
from public_service.models import Pessoa
from public_service import serializer
from django_filters.rest_framework import DjangoFilterBackend


class PessoaViewset(viewsets.ModelViewSet):
    "exibindo todas as pessoas"

    queryset = Pessoa.objects.all()
    serializer_class = serializer.PessoaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'schooling']



def schooling(request):
    if request.method == 'GET':
        return JsonResponse(dict_schooling)

def states_of_life(request):
    if request.method =='GET':
        return JsonResponse(dict_states_of_life)

def status(request):
    if request.method =='GET':
        return JsonResponse(dict_status)

def states(request):
    if request.method =='GET':
        return JsonResponse(dict_states)
