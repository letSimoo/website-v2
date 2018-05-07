from django.db import models
from django.utils.translation import ugettext_lazy as _
from library.utils import get_unique_slug
from django.contrib.auth.models import User


class Lesson(models.Model):
    YOUTUBE_VIDEO = '0'
    SCRIMBA_VIDEO = '1'
    MARKDOWN = '2'
    QUIZ = '3'
    TASK = '4'

    TYPE_CHOICES = (
        (YOUTUBE_VIDEO, 'youtube-video'),
        (SCRIMBA_VIDEO, 'scrimba-video'),
        (MARKDOWN, 'markdown'),
        (QUIZ, 'quiz'),
        (TASK, 'task'),
    )

    title = models.CharField(max_length=60, verbose_name=_('title'))
    slug = models.SlugField(max_length=140, unique=True,
                            blank=True, allow_unicode=True, verbose_name=_('slug'))
    type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, default=MARKDOWN, verbose_name=_('type'))
    url = models.URLField(verbose_name=_('url'))
    is_shown = models.ManyToManyField(User, verbose_name=_('shown users'))

    class Meta:
        verbose_name = _('lesson')
        verbose_name_plural = _('lessons')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save()

    def __str__(self):
        return f'{self.title}'


class Module(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('title'))
    slug = models.SlugField(max_length=140, unique=True,
                            blank=True, allow_unicode=True, verbose_name=_('slug'))
    lessons = models.ManyToManyField(
        Lesson, through='ModuleLesson', related_name='modules', verbose_name=_('lessons'))

    class Meta:
        verbose_name = _('module')
        verbose_name_plural = _('modules')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save()

    def __str__(self):
        return f'{self.title}'


class ModuleLesson(models.Model):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.DO_NOTHING, verbose_name=_('lesson'))
    module = models.ForeignKey(
        Module, on_delete=models.DO_NOTHING, verbose_name=_('module'))
    order = models.IntegerField(verbose_name=_('Order'), default=0)

    class Meta:
        verbose_name = _('module and lesson')
        verbose_name_plural = _('modules and lessons')
        ordering = ['order', ]


class Workshop(models.Model):
    BEGINNER = '0'
    INTERMEDIATE = '1'
    ADVANCED = '2'

    LEVEL_CHOICES = (
        (BEGINNER, 'beginner'),
        (INTERMEDIATE, 'intermediate'),
        (ADVANCED, 'advanced'),
    )

    title = models.CharField(max_length=60, verbose_name=_('title'))
    slug = models.SlugField(max_length=140, unique=True,
                            blank=True, allow_unicode=True, verbose_name=_('slug'))
    last_update_date = models.DateTimeField(
        auto_now=True, verbose_name=_('last update date'))
    level = models.CharField(
        max_length=10, choices=LEVEL_CHOICES, default=BEGINNER, verbose_name=_('type'))
    modules = models.ManyToManyField(
        Module, through='WorkshopModule', related_name='workshops', verbose_name=_('modules'))

    class Meta:
        verbose_name = _('workshop')
        verbose_name_plural = _('workshops')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save()

    def __str__(self):
        return f'{self.title}'


class WorkshopModule(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.DO_NOTHING, verbose_name=_('module'))
    workshop = models.ForeignKey(
        Workshop, on_delete=models.DO_NOTHING, verbose_name=_('workshop'))
    order = models.IntegerField(verbose_name=_('Order'), default=0)

    class Meta:
        verbose_name = _('workshop and module')
        verbose_name_plural = _('workshops and modules')
        ordering = ['order', ]


class Track(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('title'))
    slug = models.SlugField(max_length=140, unique=True,
                            blank=True, allow_unicode=True, verbose_name=_('slug'))
    workshops = models.ManyToManyField(
        Workshop, through='TrackWorkshop', related_name='tracks', verbose_name=_('workshops'))

    class Meta:
        verbose_name = _('track')
        verbose_name_plural = _('tracks')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save()

    def __str__(self):
        return f'{self.title}'


class TrackWorkshop(models.Model):
    workshop = models.ForeignKey(
        Workshop, on_delete=models.DO_NOTHING, verbose_name=_('workshop'))
    track = models.ForeignKey(
        Track, on_delete=models.DO_NOTHING, verbose_name=_('track'))
    order = models.IntegerField(verbose_name=_('Order'), default=0)

    class Meta:
        verbose_name = _('track and workshop')
        verbose_name_plural = _('tracks and workshops')
        ordering = ['order', ]