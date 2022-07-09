from django.shortcuts import render
from forums.models import Category

def homepage(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, template_name='main/index.html', context=context)