# Generated by Django 2.0.4 on 2018-05-09 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_opened_module',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='library.Module', verbose_name='last opened module'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_opened_workshop',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='library.Workshop', verbose_name='last opened workshop'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshop',
            name='authors',
            field=models.ManyToManyField(related_name='workshops', to=settings.AUTH_USER_MODEL, verbose_name='authors'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='description',
            field=models.CharField(blank=True, max_length=1000, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='duration',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3, verbose_name='duration'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshop',
            name='used_technologies',
            field=models.CharField(blank=True, max_length=100, verbose_name='used_technologies'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='workshop_result_url',
            field=models.URLField(default='wwwwww', verbose_name='markdown url'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_opened_lesson',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='library.BaseLesson', verbose_name='last opened lesson'),
        ),
    ]