# Generated by Django 4.0 on 2021-12-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_member_isdeleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='isDeleted',
            field=models.BooleanField(default='No', null=True),
        ),
    ]
