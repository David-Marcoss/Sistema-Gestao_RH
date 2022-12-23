# Generated by Django 4.1 on 2022-12-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("departamentos", "0001_initial"),
        ("funcionarios", "0003_alter_funcionario_empresa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="funcionario",
            name="departamento",
            field=models.ManyToManyField(
                blank=True, null=True, to="departamentos.departamento"
            ),
        ),
    ]
