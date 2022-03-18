# Generated by Django 4.0.3 on 2022-03-18 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookStoreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('store_name', models.CharField(max_length=50)),
                ('store_info', models.TextField()),
                ('store_img', models.CharField(max_length=255)),
                ('store_views', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'book_store',
            },
        ),
    ]
