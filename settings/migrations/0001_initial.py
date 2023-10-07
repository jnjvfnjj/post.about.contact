# Generated by Django 4.2.5 on 2023-10-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название сайта')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефонный номер')),
                ('facebook_url', models.URLField(verbose_name='Ссылка на Facebook')),
                ('instagram_url', models.URLField(verbose_name='Ссылка на Instagram')),
                ('linkeldin_url', models.URLField(verbose_name='Ссылка на Linkeldin')),
                ('logon', models.ImageField(upload_to='logo/', verbose_name='Логотип сайта')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Настройки',
                'verbose_name_plural': 'Настройка',
            },
        ),
    ]
