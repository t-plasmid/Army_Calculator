# Generated by Django 2.2.25 on 2022-01-14 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movement', '0010_auto_20211230_1313'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StartEx_Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('brigade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='startex_plan', to='movement.Brigade')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='startex_plan', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SX_Unit_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sx_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sx_unit_detail', to='startex.StartEx_Plan')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sx_unit_detail', to='movement.Unit')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SX_Vehicle_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SX_Vehicle_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('sx_u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sx_vehicle_detail', to='startex.SX_Unit_Detail')),
                ('sx_v_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sx_vehicle_detail', to='startex.SX_Vehicle_Data')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]