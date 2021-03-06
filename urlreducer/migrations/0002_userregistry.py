# Generated by Django 3.1.3 on 2021-09-20 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlreducer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_registry',
            },
        ),
    ]
