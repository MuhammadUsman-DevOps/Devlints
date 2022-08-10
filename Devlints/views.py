from django.shortcuts import render


def base(request):
    return render(request, template_name="base/base.html")


def home(request):
    return render(request, template_name="site_pages/home.html")


def about_us(request):
    return render(request, template_name="site_pages/about_us.html")


def contact_us(request):
    return render(request, template_name="site_pages/contact_us.html")


def support_faqs(request):
    return render(request, template_name="site_pages/faqs.html")
