from django.db import models

# Create your models here.


class QuestionCard(models.Model):
    word = models.CharField(max_length=128, null=False, verbose_name="Слово")
    image = models.ImageField(null=True, verbose_name="Изображение")
    translation_options = models.TextField(null=False, verbose_name="Варианты перевода")
    answer = models.CharField(max_length=128, null=False, verbose_name="Перевод")

    def __str__(self):
        return self.word

    class Meta:
        verbose_name_plural = "Карточки вопроса"
        verbose_name = "Карточки вопросов"
