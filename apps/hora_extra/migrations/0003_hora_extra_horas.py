# Generated by Django 4.1 on 2023-01-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hora_extra", "0002_hora_extra_funcionario"),
    ]

    operations = [
        migrations.AddField(
            model_name="hora_extra",
            name="horas",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]