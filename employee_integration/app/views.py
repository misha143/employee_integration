from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from datetime import datetime
import csv
from django.http import HttpResponse

import telegram
bot = telegram.Bot(token='1989836081:AAEiKOW4TH7mP1WDANebvLfyEpnjxwhawQk')

from .models import Question, Answer, Result

User = get_user_model()


@login_required
def index(request):
    quizzes = Question.objects.all()

    return render(request, 'index.html', {
        "quizzes": quizzes
    })


@login_required
def quiz_view(request, pk_quiz):
    # проверка прошёл квест или нет
    is_done = 0
    is_correct = 0

    if Result.objects.filter(question__pk=pk_quiz, user__username=request.user.username).exists():
        is_done = 1
        if Result.objects.get(question__pk=pk_quiz, user__username=request.user.username).is_correct:
            is_correct = 1

    # получаем квиз и ответы
    quiz = get_object_or_404(Question, pk=pk_quiz)
    ans_list = Answer.objects.filter(question=quiz).all()

    # сколько прошли, какой процент
    count_of_people_done = len(Result.objects.filter(question__pk=pk_quiz).all())
    count_of_people_done_correct = len(Result.objects.filter(question__pk=pk_quiz, is_correct=True).all())
    if count_of_people_done == 0:
        percent_of_done_correct = 0
    else:
        percent_of_done_correct = round(count_of_people_done_correct / count_of_people_done * 100)

    return render(request, 'quiz.html', {
        "is_done": is_done,
        "is_correct": is_correct,
        "quiz": quiz,
        "ans_list": ans_list,
        "count_of_people_done": count_of_people_done,
        "percent_of_done_correct": percent_of_done_correct
    })


@login_required
def quiz_pass(request, pk_quiz, pk_ans):
    try:
        # уникальные в связке
        user = get_object_or_404(User, username=request.user.username)
        question = get_object_or_404(Question, pk=pk_quiz)
        ans = get_object_or_404(Answer, pk=pk_ans)
        Result.objects.create(question=question, user=user, is_correct=ans.correct, answer=ans)
        bot.sendMessage(chat_id=386589423, text=f"{user.first_name} {user.last_name} прошёл тест.\n\nТест: {question}\n\nОтвет пользователя: {ans}\n\nОтвет правильный? {ans.correct}")
    except:
        # в случае если уже была создана связь
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def get_csv(request):
    now = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': f'attachment; filename="Results_{now}.csv"'},
    )

    writer = csv.writer(response)

    data = Result.objects.all()
    writer.writerow(['Имя', 'Фамилия', 'Подразделение', 'Вопрос', 'Ответ', 'Ответ правильный?'])
    for result in data:
        group_name = ''
        for group in result.user.groups.all():
            group_name = group.name
        result_correct = 0
        if result.is_correct:
            result_correct = 1
        writer.writerow(
            [result.user.first_name, result.user.last_name, group_name, result.question, result.answer, result_correct])

    return response

