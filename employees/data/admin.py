from django.contrib import admin
from data.models import Data


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = (
        'vneshnij_identifikator_dlja_importa',
        'familija',
        'imja',
        'dolzhnost',
        'mobilnyj_telefon',
        'login',
        'parol',
    )
