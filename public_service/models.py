from django.db import models
from public_service.model.states import states
from public_service.model.status import status
from public_service.model.states_of_life import states_of_life
from public_service.model.schooling import schooling

class Pessoa(models.Model):

    name = models.CharField(max_length=30, blank=False, null=False,)
    birth = models.DateField(null=False)
    cpf = models.CharField(max_length=11, blank=False, unique=True)
    e_mail = models.EmailField(max_length=250)
    states = models.CharField(max_length=100, choices=states, blank=False, null=False,)
    marital_status = models.CharField(max_length=100, choices=status, blank=False, null=False,)
    average_wage = models.PositiveIntegerField()
    schooling = models.CharField(max_length=250, choices=schooling, blank=False, null=False)
    alive = models.CharField(max_length=100, choices=states_of_life, blank=False, null=False)
     
    def __str__(self):
        return self.name
