# Generated by Django 3.2.6 on 2021-09-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_auto_20210906_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
