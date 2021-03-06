# Generated by Django 4.0.4 on 2022-05-13 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulk_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('message', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Bulk_orders',
            },
        ),
        migrations.CreateModel(
            name='General_enquiries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'General_enquiries',
            },
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', tinymce.models.HTMLField()),
                ('Mrp', models.FloatField(max_length=100)),
                ('sale_price', models.FloatField(max_length=100)),
                ('quantity', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='packages/')),
                ('status', models.CharField(choices=[('active', 'Active'), ('deactive', 'Deactive')], default='draft', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='Policies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', tinymce.models.HTMLField()),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Policies',
            },
        ),
        migrations.CreateModel(
            name='sliderimages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='slider/')),
            ],
            options={
                'verbose_name_plural': 'slider images',
            },
        ),
        migrations.CreateModel(
            name='Statelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Statelist',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('content', tinymce.models.HTMLField()),
                ('feature_image', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='our_cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('city_area', models.CharField(blank=True, max_length=100)),
                ('state_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frischboxadmin.statelist')),
            ],
            options={
                'verbose_name_plural': 'our_cities',
            },
        ),
    ]
