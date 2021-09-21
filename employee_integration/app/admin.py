from django.contrib import admin

from .models import Question, Answer, Result


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "valid_until")
    search_fields = ("title",)
    list_filter = ("created",)
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("text", "correct", "question")
    search_fields = ("text",)


class ResultAdmin(admin.ModelAdmin):
    list_display = ("question", "user", "answer", "is_correct")


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Result, ResultAdmin)
