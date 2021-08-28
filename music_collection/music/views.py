from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .models import Music, Rating
from .forms import RatingForm
# Create your views here.


class CdTemplateView(TemplateView):
    template_name = 'cd-list.html'
    extra_context = {'cds':Music.objects.all()}

def cds_dynamic_lookup_view(request, id):
    cd = Music.objects.get(id=id)
    rate = Rating.objects.filter(music=id)
    context = {
        "cds":cd,
        "ratings":rate
    }
    return render(request,"cd-details.html", context)

def rate_music(request):
    form = RatingForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list-of-cds')



    return render(request, 'rate-music.html', {'form':form})


