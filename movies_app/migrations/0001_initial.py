# Generated by Django 3.2 on 2021-04-24 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=512)),
                ('last_name', models.CharField(blank=True, max_length=512)),
                ('middle_name', models.CharField(blank=True, max_length=512)),
                ('phone_number', models.DecimalField(decimal_places=0, max_digits=10)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('prefix', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=40)),
                ('released_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='cover_image')),
                ('asin', models.CharField(max_length=10, verbose_name='ASIN')),
                ('directors', models.ManyToManyField(to='movies_app.Director')),
                ('genre', models.ManyToManyField(to='movies_app.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('prefix', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=2000)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_app.movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='studio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_app.studio'),
        ),
    ]
