# Generated by Django 3.0.7 on 2022-08-30 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_creditbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditbook',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchaseitem',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='saleitem',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='saleitem',
            name='weight',
            field=models.CharField(choices=[('kg', 'KG'), ('man', 'MAN')], default='kg', max_length=6),
        ),
        migrations.AlterField(
            model_name='creditbook',
            name='paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='creditbook',
            name='remaing',
            field=models.IntegerField(default=0),
        ),
    ]
