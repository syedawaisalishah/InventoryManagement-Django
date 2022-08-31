# Generated by Django 3.0.7 on 2022-08-25 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_purchaseitem_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.IntegerField()),
                ('remaing', models.IntegerField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creditbooksupplier', to='transactions.Supplier')),
            ],
        ),
    ]
