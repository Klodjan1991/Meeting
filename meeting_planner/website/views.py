from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})


def projects(request):
    return HttpResponse('<h1>This is list of projects</h1>')


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("I`m Reindert and I make courses for Pluralsight.")


