from django import forms
from django.core.validators import RegexValidator
from .models import QuestionCard


class QuestionCardForm(forms.ModelForm):
    word = forms.RegexField(
        regex=r'^[a-zA-Z\s]+$',
        max_length=128,
        validators=[RegexValidator(
            regex=r'^[a-zA-Z\s]+$',
            message='Поле word не прошло валидацию.',
            code='invalid_word'
        )],
        error_messages={
            'invalid': 'Слово должно включать только буквы английского алфавита и пробелы.'
        }
    )
    answer = forms.RegexField(
        regex=r'^[а-яА-Я\s]+$',
        max_length=128,
        validators=[RegexValidator(
            regex=r'^[а-яА-Я\s]+$',
            message='Поле answer не прошло валидацию.',
            code='invalid_word'
        )],
        error_messages={
            'invalid': 'Слово должно включать только буквы русского и пробелы.'
        }
    )

    class Meta:
        model = QuestionCard
        fields = ['word', 'image', 'translation_options', 'answer']
