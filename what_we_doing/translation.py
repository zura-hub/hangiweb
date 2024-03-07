from modeltranslation.translator import register, TranslationOptions
from .models import What_We_Doing

@register(What_We_Doing)
class What_We_Doing(TranslationOptions):
    fields = ('title', 'description')

