from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome',
                    'telefone', 'categoria', 'mostrar')
    list_display_links = ('nome',)
    # list_filter = ('nome', 'sobrenome') # coloca um filtro no canto
    # list_per_page = 5  # quantidade de pessoas que vai ser mostrado
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

