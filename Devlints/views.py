from django.shortcuts import render

from Devlints.models import Company, SEOSettings, Products, Statistics, Partners, Testimonials, AboutUs, Services, \
    ContactUs


def base(request):
    return render(request, template_name="base/base.html")


def home(request):
    company_info = Company.objects.first()
    seo = SEOSettings.objects.first()
    products = Products.objects.all()
    states = Statistics.objects.first()
    partners = Partners.objects.all()
    testimonials = Testimonials.objects.all()[:3]
    context = {
        "company_info": company_info,
        "products": products,
        "states": states,
        "partners": partners,
        "seo": seo,
        "testimonials": testimonials,
    }
    return render(request, template_name="site_pages/home.html", context=context)


def about_us(request):
    company_info = Company.objects.first()
    seo = SEOSettings.objects.first()
    products = Products.objects.all()
    partners = Partners.objects.all()
    about = AboutUs.objects.first()
    states = Statistics.objects.first()
    context = {
        "company_info": company_info,
        "products": products,
        "about": about,
        "partners": partners,
        "seo": seo,
        "states": states,

    }
    return render(request, template_name="site_pages/about_us.html", context=context)


def contact_us(request):
    company_info = Company.objects.first()
    seo = SEOSettings.objects.first()
    products = Products.objects.all()
    contact = ContactUs.objects.first()
    partners = Partners.objects.all()
    testimonials = Testimonials.objects.all()[:3]
    context = {
        "company_info": company_info,
        "products": products,
        "contact": contact,
        "partners": partners,
        "seo": seo,
        "testimonials": testimonials,
    }
    return render(request, template_name="site_pages/contact_us.html", context=context)


def support_faqs(request):

    return render(request, template_name="site_pages/faqs.html")


def services(request):
    company_info = Company.objects.first()
    seo = SEOSettings.objects.first()
    products = Products.objects.all()
    states = Statistics.objects.first()
    partners = Partners.objects.all()
    our_services = Services.objects.all()
    testimonials = Testimonials.objects.all()[:3]
    context = {
        "company_info": company_info,
        "products": products,
        "states": states,
        "partners": partners,
        "seo": seo,
        "testimonials": testimonials,
        "services": our_services,
    }
    return render(request, template_name="site_pages/services.html", context=context)