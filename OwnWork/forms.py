from django import forms
from datetime import datetime as dt

from .models import Article, Account

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'author', 'content', 'published']
        widgets = dict(
            content = forms.Textarea(attrs={
                'rows':18,
            }),
            published = forms.DateTimeInput(attrs={
                'type':'datetime-local',
            }),
        )

        def __init__(self, *args, **kwargs) -> None:
            super(ArticleForm, self).__init__(*args, **kwargs)

        