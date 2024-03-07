from modeltranslation.translator import register, TranslationOptions
from .models import  Employee, Team

@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('name', 'history')



@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('title', )