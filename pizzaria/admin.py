from django.contrib import admin
from .models import Cliente, Funcionarios
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    ...
    


class FuncionariosAdmin(admin.ModelAdmin):
    ...







admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Funcionarios, FuncionariosAdmin)


