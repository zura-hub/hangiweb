from modeltranslation.translator import register, TranslationOptions
from .models import Photo, Title

@register(Photo)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('description', 'header')


@register(Title)
class TitlesTranslationOptions(TranslationOptions):
    fields = ('header',)