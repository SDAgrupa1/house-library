from django.shortcuts import render
from .models import Music
from django.views.generic import TemplateView
from .models import Music
# Create your views here.


class CdTemplateView(TemplateView):
    template_name = 'cd-list.html'
    extra_context = {'cds':Music.objects.all()}

def cds_dynamic_lookup_view(request, id):
    cd = Music.objects.get(id=id)
    context = {
        "cds":cd
    }
    return render(request,"cd-details.html", context)