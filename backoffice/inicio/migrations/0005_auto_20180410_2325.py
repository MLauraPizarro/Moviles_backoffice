# Generated by Django 2.0.3 on 2018-04-10 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_persona_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='url',
            field=models.TextField(blank=True, editable=False, max_length=250),
        ),
        migrations.AlterField(
            model_name='persona',
            name='url',
            field=models.TextField(blank=True, editable=False, max_length=250),
        ),
        migrations.AlterField(
            model_name='receta',
            name='foto',
            field=models.FileField(blank=True, upload_to='recetas'),
        ),
    ]
