# Generated by Django 3.2.15 on 2023-03-06 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ca298shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='colour',
            field=models.ForeignKey(default='Blue', on_delete=django.db.models.deletion.CASCADE, to='ca298shop.colour'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.ForeignKey(default='M', on_delete=django.db.models.deletion.CASCADE, to='ca298shop.size'),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.ForeignKey(default='Top', on_delete=django.db.models.deletion.CASCADE, to='ca298shop.type'),
        ),
    ]