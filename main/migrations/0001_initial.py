<<<<<<< HEAD
# Generated by Django 3.0.7 on 2020-06-29 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_content', models.TextField()),
                ('blog_posted', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
=======
# Generated by Django 3.0.7 on 2020-06-29 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_content', models.TextField()),
                ('blog_posted', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
>>>>>>> bc1000db8c48c1e68896bc37fe6e054a1877830a
