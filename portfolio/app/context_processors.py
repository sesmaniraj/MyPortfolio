from . models import *


def about(request):
    about = AboutMe.objects.first()
    exp=Experience.objects.all()
    skill=Skills.objects.all()
    portfolio=Portfolio.objects.all()
    

    return({
        'about':about,
        'exp':exp,
        'skills':skill,
        'porfolio':portfolio

    })
