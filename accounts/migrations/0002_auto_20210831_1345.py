# Generated by Django 3.2 on 2021-08-31 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('cu', 'customers'), ('su', 'supporter'), ('se', 'sellers')], max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='customeuser',
            name='phone_number',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator('^09(1[0-9]|3[1-9]|2[0-9]|0[1-9])-?[0-9]{3}-?[0-9]{4}$', 'only valid mobile phone  is required')], verbose_name='شماره موبایل'),
        ),
        migrations.AddField(
            model_name='customeuser',
            name='role',
            field=models.ManyToManyField(to='accounts.role'),
        ),
    ]
