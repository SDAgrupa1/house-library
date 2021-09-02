from django.shortcuts import render
from django.shortcuts import redirect


def home_view(request):
    return render(
        request,
        template_name="home.html"
    )


def about_us_view(request):
    return render(
        request,
        template_name="about_us.html"
    )


def error_404_view(request):
    return render(
        request,
        template_name="404.html"
    )


def redirect_root(request):
    return redirect("/home/")
