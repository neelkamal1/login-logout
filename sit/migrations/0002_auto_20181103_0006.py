# Generated by Django 2.1.2 on 2018-11-03 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.DeleteModel(
            name='newf',
        ),
    ]
