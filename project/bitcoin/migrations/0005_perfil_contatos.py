# Generated by Django 2.0.5 on 2018-06-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin', '0004_convite'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='contatos',
            field=models.ManyToManyField(related_name='_perfil_contatos_+', to='bitcoin.Perfil'),
        ),
    ]
