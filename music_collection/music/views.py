from django.shortcuts import render
from .models import Music
from django.views.generic import TemplateView
from .models import Music
# Create your views here.


class CdTemplateView(TemplateView):
    template_name = 'cd-list.html'
    extra_context = {'cds':Music.objects.all()}