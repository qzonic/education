from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from martor.models import MartorField

from .utils import get_material_upload_path, get_slide_upload_path


class Material(models.Model):
    """
    Material model.
    """

    class Type(models.TextChoices):
        ARTICLE = ('article', _('Статья'))
        VIDEO = ('video', _('Видео'))
        PRESENTATION = ('presentation', _('Презентация'))

    material_type = models.CharField(
        max_length=20,
        choices=Type.choices,
        verbose_name=_('Тип'),
    )
    title = models.CharField(
        max_length=1024,
        verbose_name=_('Название'),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Описание'),
    )
    slug = models.SlugField()
    image = models.ImageField(
        upload_to=get_material_upload_path,
        verbose_name=_('Изображение'),
    )
    content = MartorField(
        null=True,
        blank=True,
        verbose_name=_('Контент'),
    )
    video = models.FileField(
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["mp4", "avi", "mov", "mkv"])],
        verbose_name=_('Видео'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Создано'),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Обновлено'),
    )
    key_words = models.TextField(
        verbose_name=_('Ключевые слова'),
        help_text=_('Слова перечисляются через запятую'),
    )

    class Meta:
        verbose_name = _('Материал')
        verbose_name_plural = _('Материалы')
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Slide(models.Model):
    """
    Slide model for presentation material.
    """

    material = models.ForeignKey(
        to=Material,
        on_delete=models.CASCADE,
        verbose_name=_('Материал'),
    )
    slide = models.ImageField(
        upload_to=get_slide_upload_path,
        verbose_name=_('Слайд'),
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Порядок'),
    )

    class Meta:
        verbose_name = _('Слайд')
        verbose_name_plural = _('Слайды')
        ordering = ('order',)
