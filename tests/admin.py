from django.contrib import admin
from .models import AnswerOption, Question, TestResult


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_number', 'text', 'temperament')
    list_filter = ('temperament',)
    search_fields = ('text',)


@admin.register(AnswerOption)
class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'score')


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'dominant_temperament',
        'sangvinik_score',
        'xolerik_score',
        'flegmatik_score',
        'melanxolik_score',
        'created_at',
    )
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
