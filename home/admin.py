from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from solo.admin import SingletonModelAdmin

from models import Portfolio, Projects, TechnicalExpertise, Items, Quotes


class ProjectsInlineAdmin(admin.TabularInline):
    model = Projects
    extra = 1


class QuotesInlineAdmin(admin.TabularInline):
    model = Quotes
    extra = 1


class TechnicalExpertiseInlineAdmin(admin.TabularInline):
    model = TechnicalExpertise
    extra = 1
    filter_horizontal = ['items', ]


class PortfolioAdmin(SingletonModelAdmin):
    list_display = ['__unicode__', 'email', 'city', ]
    fieldsets = [
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number',
                                         'gender', 'date_of_birth', 'address', 'pin', 'city',
                                         'country', 'website', 'about_me')}),
        (_('Image'), {'fields':('profile_image', )}),
        (_('Social media links'), {'fields':('facebook', 'twitter', 'linked_in',
                                             'stack_overflow', 'github')}),
        (_('Activity'), {'fields':('number_of_clients', 'number_of_projects',
                                   'number_of_lines_of_code')}),
        (_('Summery'), {'fields':('career_objective', 'employment_profile', 'academic_record',
                                  'personal_skills')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    ]
    inlines = [ProjectsInlineAdmin, TechnicalExpertiseInlineAdmin, QuotesInlineAdmin]

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Items)
