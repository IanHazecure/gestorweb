# Generated by Django 5.0.6 on 2025-06-12 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='herramientas',
            name='name',
            field=models.CharField(default='Sin nombre', max_length=200),
        ),
        migrations.AddField(
            model_name='pinturas',
            name='name',
            field=models.CharField(default='Sin nombre', max_length=200),
        ),
        migrations.AddField(
            model_name='sellantes',
            name='name',
            field=models.CharField(default='Sin nombre', max_length=200),
        ),
    ]
