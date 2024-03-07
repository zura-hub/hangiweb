from modeltranslation.translator import register, TranslationOptions
from .models import Phartner, MainTitle

@register(Phartner)
class PhartnerTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(MainTitle)
class MainTranslationOptions(TranslationOptions):
    fileds = ('title')