# Generated by Django 4.1 on 2022-10-10 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShaRoSa', '0004_rename_user_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='charge',
            field=models.IntegerField(max_length=5),
        ),
    ]
