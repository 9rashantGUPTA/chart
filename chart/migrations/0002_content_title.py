# Generated by Django 2.2.4 on 2020-06-18 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Brand'),
        ),
    ]
