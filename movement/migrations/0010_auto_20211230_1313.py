# Generated by Django 2.2.25 on 2021-12-30 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movement', '0009_auto_20211227_2304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cp_detail',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='packet_detail',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='unit_detail',
            options={'ordering': ['id']},
        ),
    ]