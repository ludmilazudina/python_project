from django.urls import path
from .views import exercise_card, create_card_view, finish_training

urlpatterns = [
    path('card/<int:exercise_id>', exercise_card, name='exercise_card'),
    path('card/create', create_card_view, name='card_create'),
    path('finish', finish_training, name='finish_training')
]
