# Generated by Django 4.2.6 on 2023-11-08 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at')),
                ('last_modified_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre: ')),
                ('abv', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Volumén de Alcohol')),
                ('is_filter', models.BooleanField(default=False, verbose_name='¿Está Filtrado?')),
                ('color', models.SmallIntegerField(choices=[(1, 'Yello'), (2, 'Black'), (3, 'Amber'), (4, 'Brown')], default=1, verbose_name='Color')),
                ('image', models.ImageField(blank=True, null=True, upload_to='beer', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Beer',
                'verbose_name_plural': 'Beers',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='SpecialIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at')),
                ('last_modified_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('beers', models.ManyToManyField(blank=True, related_name='special_ingredients', to='beers.beer')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creted by')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'verbose_name': 'Sepecial Ingredient',
                'verbose_name_plural': 'Special Ingredients',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at')),
                ('last_modified_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('tax_number', models.IntegerField(unique=True, verbose_name='Código')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creted by')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='beer',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beers', to='beers.company'),
        ),
        migrations.AddField(
            model_name='beer',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Creted by'),
        ),
        migrations.AddField(
            model_name='beer',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
    ]
