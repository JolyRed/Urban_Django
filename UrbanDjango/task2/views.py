from django.shortcuts import render # type: ignore
from django.views.generic import TemplateView
# Create your views here.

class class_temp(TemplateView):
    template_name = 'second_task/class_template.html'


def func_temp(request):
    return render(request, 'second_task/func_template.html')
