from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from .models import MusicAlbum, Rating, Performer
from .forms import RatingForm, MusicForm, PerformerForm


# Create your views here.


class CdTemplateView(TemplateView):
    template_name = 'cd-list.html'
    extra_context = {'cds': MusicAlbum.objects.all()}


def cds_dynamic_lookup_view(request, id):
    cd = MusicAlbum.objects.get(id=id)
    rate = Rating.objects.filter(music=id)
    context = {
        "cds": cd,
        "ratings": rate
    }
    return render(request, "cd-details.html", context)


def rate_music(request):
    form = RatingForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('music-urls:list-of-cds')

    return render(request, 'rate-music.html', {'form': form})


def new_music_album(request):
    form = MusicForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('music-urls:list-of-cds')
    return render(request, 'cd_music_form.html', {'form': form})


def all_music_albums(request):
    music_albums = MusicAlbum.objects.all()
    return render(request, "cd-list.html", {'cd.info': music_albums})


def edit_music_album(request, id):
    music = get_object_or_404(MusicAlbum, pk=id)
    form = MusicForm(request.POST or None, request.FILES or None, instance=music)

    if form.is_valid():
        form.save()
        return redirect('music-urls:list-of-cds')
    return render(request, 'cd_music_form.html', {'form': form})


def delete_music_album(request, id):
    music = get_object_or_404(MusicAlbum, pk=id)

    if request.method == "POST":
        music.delete()
        return redirect('music-urls:list-of-cds')

    return render(request, 'sure.html', {'music': music})




# PERFORMER
# Create # Read #Update # Delete

class PerformerTemplateView(TemplateView):
    template_name = 'performer_list.html'
    extra_context = {'performer': Performer.objects.all()}


def performer_dynamic_lookup_view(request, id):
    name = Performer.objects.get(id=id)
    context = {
        "performer_list": name,
    }
    return render(request, "performer-details.html", context)


def new_performer(request):
    form = PerformerForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(PerformerForm)
    return render(request, 'performer_form.html', {'form': form})


def list_performer(request):
    performer_list = Performer.objects.all()
    return render(request, "performer_list.html", {'performer.new': performer_list})


def edit_performer(request, id):
    performer = get_object_or_404(Performer, pk=id)
    form = PerformerForm(request.POST or None, request.FILES or None, instance=performer)

    if form.is_valid():
        form.save()
        return redirect('music-urls:list_performer')
    return render(request, 'performer_form.html', {'form': form})


def delete_performer(request, id):
    performer = get_object_or_404(Performer, pk=id)

    if request.method == "POST":
        performer.delete()
        return redirect('music-urls:list_performer')

    return render(request, 'performer_sure.html', {'performer': performer})

