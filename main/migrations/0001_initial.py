# Generated by Django 3.0.5 on 2020-04-26 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('edited_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('edited_date', models.DateTimeField(auto_now=True, verbose_name='date last edited')),
                ('body', models.TextField(verbose_name='the actual blog post')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('link', models.CharField(blank=True, default='', max_length=500)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projects/')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
