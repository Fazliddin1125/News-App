# Generated by Django 4.0 on 2023-06-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_category_name_en_category_name_ru_category_name_uz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='body_en',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='body_ru',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='body_uz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='body_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='body_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='body_uz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_uz',
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='PB', max_length=2),
        ),
    ]