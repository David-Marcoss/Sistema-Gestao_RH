from rest_framework import serializers
from apps.funcionarios.models import Funcionario
from apps.hora_extra.api.serializers import Hora_ExtraSerializer

# Serializers define the API representation.
class FuncionarioSerializer(serializers.ModelSerializer):
    horas_extras = Hora_ExtraSerializer(many = True)
    class Meta:
        model = Funcionario
        fields = ['id','nome','user', 'empresa', 'departamento','get_total_horas_ex_utilizadas','horas_extras']


