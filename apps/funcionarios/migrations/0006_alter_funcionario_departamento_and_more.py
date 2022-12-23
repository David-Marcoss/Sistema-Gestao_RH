# Generated by Django 4.1 on 2022-12-23 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0001_initial"),
        ("departamentos", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("funcionarios", "0005_rename_empresa_funcionario_empresa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="funcionario",
            name="departamento",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="funcionarios",
                to="departamentos.departamento",
            ),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="empresa",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="funcionarios",
                to="empresa.empresa",
            ),
        ),
        migrations.AlterField(
            model_name="funcionario",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
