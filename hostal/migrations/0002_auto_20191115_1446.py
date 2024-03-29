# Generated by Django 2.2.7 on 2019-11-15 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comedor2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreplato', models.CharField(max_length=100, null=True, verbose_name='Nombre Plato')),
                ('descripcion', models.CharField(max_length=100, null=True, verbose_name='Plato Descripcion')),
                ('precio', models.IntegerField(max_length=100, null=True, verbose_name='Precio Menu')),
                ('servicio', models.CharField(max_length=100, null=True, verbose_name='Plato Descripcion')),
            ],
        ),
        migrations.RenameField(
            model_name='comedor',
            old_name='Postre',
            new_name='postre',
        ),
        migrations.AddField(
            model_name='comedor',
            name='nombre',
            field=models.CharField(max_length=100, null=True, verbose_name='Nombre Menu'),
        ),
        migrations.AddField(
            model_name='comedor',
            name='precio',
            field=models.IntegerField(max_length=100, null=True, verbose_name='Precio Menu'),
        ),
    ]
