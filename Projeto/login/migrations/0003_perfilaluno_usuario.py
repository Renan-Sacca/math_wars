# Generated by Django 2.1.4 on 2021-05-05 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_perfilaluno_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilaluno',
            name='usuario',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]