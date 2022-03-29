# Generated by Django 4.0.3 on 2022-03-23 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_alter_dealer_address_alter_dealer_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=15, unique=True, verbose_name='Phone Number'),
            preserve_default=False,
        ),
    ]