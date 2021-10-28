from django.contrib import admin

from .models import Question, Answer, Result, Quiz


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    search_fields = ("title",)
    list_filter = ("created",)
    inlines = [AnswerInline]


class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    search_fields = ("title",)
    list_filter = ("created",)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("text", "correct", "question")
    search_fields = ("text",)


class ResultAdmin(admin.ModelAdmin):
    list_display = ("question", "user", "answer", "is_correct", "time_result_done")
    list_filter = ("question",)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Quiz, QuizAdmin)
