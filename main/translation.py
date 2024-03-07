from modeltranslation.translator import register, TranslationOptions
from .models import About, Mission, Activities, lists, Contact

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(Mission)
class MissionTranslationOptions(TranslationOptions):
    fields = ('headers', 'content')

@register(Activities)
class ActivitiesTranslationOptions(TranslationOptions):
    fields = ('header', 'content')


@register(lists)
class ListsTranslationOptions(TranslationOptions):
    fields = ('home', 'social', 'gallery', 'team', 'project', 'done', 'doing', 'partnership', 'apps', 'contact', 'meniu')


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields =( 'city', 'address', )