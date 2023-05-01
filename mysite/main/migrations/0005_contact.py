# Generated by Django 4.2 on 2023-05-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_book_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Contact user name')),
                ('email', models.EmailField(max_length=254, verbose_name='Contact user email')),
                ('subject', models.CharField(max_length=255, verbose_name='Contact subject')),
                ('message', models.TextField(verbose_name='Contact message')),
            ],
        ),
    ]