from modeltranslation.translator import register, TranslationOptions
from .models import What_We_Do

@register(What_We_Do)
class What_We_DoTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )