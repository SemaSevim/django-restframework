# Generated by Django 4.0.6 on 2022-07-27 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_question_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Makale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazar', models.CharField(max_length=150)),
                ('baslik', models.CharField(max_length=120)),
                ('aciklama', models.CharField(max_length=200)),
                ('metin', models.TextField()),
                ('sehir', models.BooleanField(default=True)),
                ('yayımlanma_tarihi', models.DateField()),
                ('aktif', models.BooleanField(default=True)),
                ('yaratilma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('güncelleme_tarihi', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
