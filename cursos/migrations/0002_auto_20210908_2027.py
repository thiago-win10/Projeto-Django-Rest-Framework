# Generated by Django 2.2.9 on 2021-09-08 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'ordering': ['id'], 'verbose_name': 'Avaliacão', 'verbose_name_plural': 'Avaliações'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['id'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
    ]
