# Generated by Django 3.2.15 on 2022-08-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Devlints', '0003_auto_20220830_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='SEOSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_author', models.TextField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('meta_keywords', models.TextField(blank=True, null=True)),
                ('meta_type', models.TextField(blank=True, null=True)),
                ('meta_title', models.TextField(blank=True, null=True)),
                ('meta_url', models.TextField(blank=True, null=True)),
                ('meta_site_name', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'SEO Settings',
                'verbose_name_plural': 'SEO Settings',
            },
        ),
    ]
