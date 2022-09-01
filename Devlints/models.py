from ckeditor.fields import RichTextField
from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=2000)
    description = models.TextField(null=True, blank=True)
    thumbnail_small = models.ImageField(upload_to="images/products", null=True, blank=True)
    thumbnail_large = models.ImageField(upload_to="images/products", null=True, blank=True)
    feature_1 = models.TextField(null=True, blank=True)
    feature_2 = models.TextField(null=True, blank=True)
    feature_3 = models.TextField(null=True, blank=True)
    feature_4 = models.TextField(null=True, blank=True)

    is_featured = models.BooleanField(default=False, help_text="Featured product will be shown on banner.")
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"


class Statistics(models.Model):
    title = models.CharField(max_length=1000)
    total_products = models.IntegerField()
    monthly_users = models.IntegerField()
    working_hours = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Statistics"
        verbose_name_plural = "Statistics"


class Testimonials(models.Model):
    picture = models.ImageField(upload_to="images/testimonials")
    name = models.CharField(max_length=500, null=True, blank=True)
    comment = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Testimonials"
        verbose_name_plural = "Testimonials"


class Partners(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    partner_logo = models.ImageField(upload_to="images/partners")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Partners"
        verbose_name_plural = "Partners"


class AboutUs(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to="images/office")
    vision = models.TextField()
    mission = models.TextField()
    values = RichTextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class ContactUs(models.Model):
    phone_number = models.CharField(max_length=100)
    email_address = models.EmailField()
    physical_address = models.TextField()
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.physical_address

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"


class Services(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"


class Company(models.Model):
    name = models.CharField(max_length=100)
    tag_line = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField( null=True, blank=True)
    logo = models.ImageField(upload_to="images/company", null=True, blank=True)
    favicon = models.ImageField(upload_to="images/company", null=True, blank=True)
    banner_background_image = models.ImageField(upload_to="images/company", null=True, blank=True)
    banner_foreground_image = models.ImageField(upload_to="images/company", null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company Info"
        verbose_name_plural = "Company Info"


class EULA(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    content = RichTextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "EULA"
        verbose_name_plural = "EULA"


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    content = RichTextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Privacy Policy"
        verbose_name_plural = "Privacy Policy"


class TermsAndConditions(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    content = RichTextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Terms & Conditions"
        verbose_name_plural = "Terms & Conditions"


class GDPRCompliance(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    content = RichTextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "GDPR Compliance"
        verbose_name_plural = "GDPR Compliance"


class SEOSettings(models.Model):
    meta_author = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    meta_type = models.TextField(null=True, blank=True)
    meta_title = models.TextField(null=True, blank=True)
    meta_url = models.TextField(null=True, blank=True)
    meta_site_name = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meta_author

    class Meta:
        verbose_name = "SEO Settings"
        verbose_name_plural = "SEO Settings"
