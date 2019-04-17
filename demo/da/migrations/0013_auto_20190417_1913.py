# Generated by Django 2.2 on 2019-04-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('da', '0012_auto_20190417_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outbreakform',
            name='disease',
            field=models.CharField(choices=[('Acute Haemorrhagic Fever Syndrome', 'Acute Haemorrhagic Fever Syndrome'), ('Anthrax', 'Anthrax'), ('Chikungunya', 'Chikungunya'), ('Cholera', 'Cholera'), ('Dengue', 'Dengue'), ('Ebola', 'Ebola'), ('Hepatitis', 'Hepatitis'), ('Malaria', 'Malaria'), ('MonkeyPox', 'MonkeyPox'), ('Plague', 'Plague'), ('Typhoid fever', 'Typhoid fever'), ('Yellow Fever', 'Yellow Fever'), ('Zika', 'Zika')], max_length=30),
        ),
    ]
