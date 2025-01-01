from django.contrib import admin
from .models import Subject, Course, Lecture

from django_summernote.admin import SummernoteModelAdmin
from .models import Text


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class LectureInline(admin.StackedInline):
    model = Lecture


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [LectureInline]


class TextAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Text, TextAdmin)