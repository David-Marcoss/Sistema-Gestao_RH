# Generated by Django 4.1 on 2022-12-22 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("funcionarios", "0002_funcionario_empresa_funcionario_departamento_and_more"),
        ("hora_extra", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="hora_extra",
            name="funcionario",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="funcionarios.funcionario",
            ),
            preserve_default=False,
        ),
    ]
