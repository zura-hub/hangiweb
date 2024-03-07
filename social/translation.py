from modeltranslation.translator import register, TranslationOptions
from .models import Blogs, Stories, Title

@register(Blogs)
class BlogsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Stories)
class StoriesTranslationOptions(TranslationOptions):
    fields = ('title', 'text')



@register(Title)
class TitlesTranslationOptions(TranslationOptions):
    fields = ('header',)