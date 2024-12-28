from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput

class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title','anons','text','date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
        }