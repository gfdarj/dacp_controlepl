# Generated by Django 4.2.1 on 2023-06-05 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_alter_controlereuniao_tem_ata_assinada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlereuniao',
            name='comissao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cadastro.comissao'),
            preserve_default=False,
        ),
    ]