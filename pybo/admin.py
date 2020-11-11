from django.contrib import admin

# Register your models here.
from pybo.models import Question, Answer
from django.db.models import Count


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    list_display = ['id', 'subject', 'author', 'create_date', 'modify_date', 'vote_count', 'comment_count']
    list_display_links = ['id', 'subject']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(vote_count=Count("voter"), comment_count=Count("comment"))
        return queryset

    def vote_count(self, obj):
        return obj.vote_count

    def comment_count(self, obj):
        return obj.comment_count


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content']
    list_display = ['id', 'content', 'question', 'create_date', 'modify_date', 'vote_count']
    list_display_links = ['id', 'content', 'question']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(vote_count=Count("voter"))
        return queryset

    def vote_count(self, obj):
        return obj.vote_count


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)