# Generated by Django 4.0.3 on 2022-03-28 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0009_alter_item_price_alter_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]