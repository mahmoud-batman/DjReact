# Generated by Django 2.2.7 on 2020-07-20 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Children')], max_length=1),
        ),
    ]
