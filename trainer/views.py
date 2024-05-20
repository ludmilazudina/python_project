from django.shortcuts import render

from .forms import QuestionCardForm
from .models import QuestionCard


def exercise_card(request, exercise_id):
    current_exercise = QuestionCard.objects.filter(pk=exercise_id).first()
    last_exercise = QuestionCard.objects.latest('id')

    if current_exercise:
        translations = current_exercise.translation_options.split(',')
        context = {'exercise': current_exercise, 'translations': translations, 'last_exercise_id': last_exercise.id}
        return render(request, 'trainer/exercise_card.html', context)

    return render(request, 'trainer/no_more_cards_template.html')


def create_card_view(request):
    if request.method == 'POST':
        form = QuestionCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'trainer/success_create_card.html')
    else:
        form = QuestionCardForm()

    return render(request, 'trainer/create_card_form.html', {'form': form})


def main_page(request):
    return render(request, 'trainer/main_page.html')


def finish_training(request):
    return render(request, 'trainer/exercise_finished.html')
