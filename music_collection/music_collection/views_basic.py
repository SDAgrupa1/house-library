from django.shortcuts import render


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
