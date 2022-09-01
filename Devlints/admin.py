from django.contrib import admin

from Devlints.models import Company, Statistics, AboutUs, ContactUs, EULA, PrivacyPolicy, TermsAndConditions, \
    GDPRCompliance, Products, Testimonials, Partners, Services, SEOSettings

admin.site.index_title = "Devlints | Admin Panel"
admin.site.site_title = "Devlints | Admin Panel"
admin.site.site_header = "Devlints | Admin Panel"


class CompanyAdminModel(admin.ModelAdmin):
    list_display = ['name', 'tag_line', 'logo', 'favicon']

    def has_add_permission(self, request):
        return not Company.objects.exists()


class ProductsAdminModel(admin.ModelAdmin):
    ist_display = ['product_name', 'thumbnail_small', 'thumbnail_large']


class StatisticsAdminModel(admin.ModelAdmin):
    list_display = ['title', 'total_products', 'monthly_users', 'working_hours']

    def has_add_permission(self, request):
        return not Statistics.objects.exists()


class TestimonialAdminModel(admin.ModelAdmin):
    list_display = ['picture', 'name', 'comment', 'created', 'updated']


class PartnersModel(admin.ModelAdmin):
    list_display = ['name', 'partner_logo', 'created', 'updated']


class AboutUsAdminModel(admin.ModelAdmin):
    list_display = ['title', 'thumbnail']

    def has_add_permission(self, request):
        return not AboutUs.objects.exists()


class ContactUsAdminModel(admin.ModelAdmin):
    list_display = ['phone_number', 'email_address', 'created', 'updated']

    def has_add_permission(self, request):
        return not ContactUs.objects.exists()


class ServicesAdminModel(admin.ModelAdmin):
    list_display = ['icon', 'title', 'created', 'updated']


class EULAAdminModel(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']

    def has_add_permission(self, request):
        return not EULA.objects.exists()


class PrivacyPolicyAdminModel(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']

    def has_add_permission(self, request):
        return not PrivacyPolicy.objects.exists()


class TermsAndConditionsAdminModel(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']

    def has_add_permission(self, request):
        return not TermsAndConditions.objects.exists()


class GDPRComplianceAdminModel(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']

    def has_add_permission(self, request):
        return not GDPRCompliance.objects.exists()


class SEOSettingsAdminModel(admin.ModelAdmin):
    list_display = ['meta_author', 'meta_type', 'meta_title']

    def has_add_permission(self, request):
        return not SEOSettings.objects.exists()


admin.site.register(Products, ProductsAdminModel)
admin.site.register(Statistics, StatisticsAdminModel)
admin.site.register(Testimonials, TestimonialAdminModel)
admin.site.register(Partners, PartnersModel)
admin.site.register(AboutUs, AboutUsAdminModel)
admin.site.register(ContactUs, ContactUsAdminModel)
admin.site.register(Services, ServicesAdminModel)
admin.site.register(Company, CompanyAdminModel)
admin.site.register(EULA, EULAAdminModel)
admin.site.register(PrivacyPolicy, PrivacyPolicyAdminModel)
admin.site.register(TermsAndConditions, TermsAndConditionsAdminModel)
admin.site.register(GDPRCompliance, GDPRComplianceAdminModel)
admin.site.register(SEOSettings, SEOSettingsAdminModel)
