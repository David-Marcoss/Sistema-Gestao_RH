# Generated by Django 4.1 on 2023-04-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hora_extra", "0005_hora_extra_horas_utilizadas_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hora_extra",
            name="horas_utilizadas",
            field=models.BooleanField(default=False),
        ),
    ]