from django.contrib import admin

from .models import (
    Student,
    StudentInfo,
    Publisher,
    Article,
    Category,
    Shop
)


admin.site.register(Student)
# admin.site.register(StudentInfo)
admin.site.register(Publisher)
admin.site.register(Article)

admin.site.register(Category)
admin.site.register(Shop)


@admin.register(StudentInfo)
class StudentInfo(admin.ModelAdmin):
    list_display = ('pass_id', 'email', 'student')
