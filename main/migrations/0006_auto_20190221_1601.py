# Generated by Django 2.1.7 on 2019-02-21 16:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190221_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='tutorialcategory',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='tutorial',
            name='slug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='tutorialcategory',
            name='slug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='tutorialcategory',
            name='summary',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 16, 0, 37, 346686), verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='tutorialseries',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialSeries', verbose_name='Series'),
        ),
    ]
