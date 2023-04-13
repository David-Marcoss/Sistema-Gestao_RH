from rest_framework import serializers
from apps.hora_extra.models import Hora_extra

# Serializers define the API representation.
class Hora_ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hora_extra
        fields = ['motivo','horas', 'horas_utilizadas']


