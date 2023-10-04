# Generated by Django 4.2.4 on 2023-09-24 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_comments', models.DateTimeField(auto_created=True, verbose_name='Дата та час')),
                ('email', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=30, verbose_name='Автор')),
                ('description', models.TextField(max_length=1000, verbose_name='Коментар')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Коментар',
                'verbose_name_plural': 'Коментарі',
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
