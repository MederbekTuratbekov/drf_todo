from django.contrib import admin
from .models import Todo, Type
from modeltranslation.admin import TranslationAdmin


class TabbedTranslationMedia:
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Type)
class TypeAdmin(TabbedTranslationMedia, TranslationAdmin):
    pass


@admin.register(Todo)
class TodoAdmin(TabbedTranslationMedia, TranslationAdmin):
    pass
