from django.shortcuts import render
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render


# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a la página principal de mi sitio Django.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "Estas viendo las respuestas de la pregunta %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))