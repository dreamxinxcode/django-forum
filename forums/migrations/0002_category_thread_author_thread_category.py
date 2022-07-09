# Generated by Django 4.0.2 on 2022-07-07 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_avatar'),
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='thread',
            name='author',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='category',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='forums.category'),
            preserve_default=False,
        ),
    ]