from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-ques_pubdate')
    context = {'question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    response = "Question id %s"
    return HttpResponse(response % question_id)


def results(request, question_id):
    response = "Results for question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "You're voting on question %s"
    return HttpResponse(response % question_id)


def show_a_question_example(request, question_id):
    response = Question.objects.get(id=question_id)
    return HttpResponse(response)
