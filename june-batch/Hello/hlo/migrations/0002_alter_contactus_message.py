# Generated by Django 4.2.5 on 2023-10-03 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='Message',
            field=models.TextField(),
        ),
    ]