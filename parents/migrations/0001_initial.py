# Generated by Django 2.1.7 on 2019-03-21 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=11)),
                ('occopation', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
    ]
