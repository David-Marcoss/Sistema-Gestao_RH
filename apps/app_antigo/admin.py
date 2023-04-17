from django.contrib import admin
from .models import Teste_Db_Antigo,registro_funcionarios

# Register your models here.


class registro_funcionariosAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return registro_funcionarios.objects.using('antigo').all()
    

admin.site.register(Teste_Db_Antigo)
admin.site.register(registro_funcionarios,registro_funcionariosAdmin)
