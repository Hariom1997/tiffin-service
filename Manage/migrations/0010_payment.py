# Generated by Django 3.1.6 on 2021-06-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manage', '0009_auto_20210529_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('Pid', models.AutoField(primary_key=True, serialize=False)),
                ('cardowner', models.CharField(max_length=100)),
                ('cardnumber', models.IntegerField(max_length=16)),
                ('month', models.IntegerField(max_length=2)),
                ('year', models.IntegerField(max_length=4)),
                ('cvv', models.IntegerField(max_length=3)),
            ],
        ),
    ]
