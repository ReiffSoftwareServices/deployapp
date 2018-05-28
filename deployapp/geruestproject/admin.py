from django.contrib import admin
from .models import Firma, Ansprechpartner, Inventar, Projekt, Geruestbuch, Equipments


class AnsprechpartnerInline(admin.TabularInline):
    model= Ansprechpartner


class AnsprechpartnerAdmin(admin.ModelAdmin):
    list_display= ('Nachname', 'Vorname', 'Firma', 'Telefon')

admin.site.register(Ansprechpartner, AnsprechpartnerAdmin)

class FirmaAdmin(admin.ModelAdmin):

    list_display= ('Name', 'Stadt', 'Ansprechpartner')

    #def get__Ansprechpartner(self, obj):
    #    return obj.Ansprechpartner.Nachname

    search_fields = ('Name', )
    inlines= [AnsprechpartnerInline, ]



admin.site.register(Firma, FirmaAdmin)



admin.site.register(Inventar)
admin.site.register(Projekt)



class EquipmentsInline(admin.TabularInline):
    model= Equipments

class GeruestbuchAdmin(admin.ModelAdmin):
    inlines= [EquipmentsInline, ]

    list_display= ('Projekt', 'Mietwochen', 'Status', 'Preis')
    raw_id_fields= ('Projekt', )
    list_filter= ('Projekt', )

admin.site.register(Geruestbuch, GeruestbuchAdmin)
