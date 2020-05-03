from django.contrib import admin
from authors.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'email_domain', 'level')
    list_display_links = ('id', '__str__')

    empty_value_display = 'not stated'

    def email_domain(self, obj):
        if obj.email:
            return obj.email.partition('@')[2]

    email_domain.empty_value_display = '[email not stated]'
# admin.site.register(Author, AuthorAdmin)
