# Generated by Django 4.1 on 2023-01-04 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0001_initial"),
        ("hora_extra", "0003_hora_extra_horas"),
    ]

    operations = [
        migrations.AddField(
            model_name="hora_extra",
            name="empresa",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="horas_extras",
                to="empresa.empresa",
            ),
            preserve_default=False,
        ),
    ]
