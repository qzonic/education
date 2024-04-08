from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Material, Slide


class MaterialForm(ModelForm):

    class Meta:
        model = Material
        fields = '__all__'

    def clean(self):
        material_type = self.cleaned_data['material_type']
        if material_type == Material.Type.VIDEO.value and not self.cleaned_data['video']:
            raise ValidationError(_('Видео материал должен иметь видео файл.'))
        elif material_type != Material.Type.VIDEO.value and self.cleaned_data['video']:
            raise ValidationError(_('Видео файл можно добавить только видео материалу.'))
        return super().clean()


class SlideForm(ModelForm):

    class Meta:
        model = Slide
        fields = (
            'slide',
            'order',
        )

    def clean(self):
        material = self.cleaned_data['material']
        if material.material_type != Material.Type.PRESENTATION.value:
            raise ValidationError(_('Только презентация может иметь слайды.'))
        return super().clean()


class SlideInline(admin.TabularInline):
    """
    Inline form for slides.
    """

    model = Slide
    form = SlideForm


class MaterialAdmin(admin.ModelAdmin):
    """
    Material admin model.
    """

    list_display = (
        'title',
        'slug',
        'material_type',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'material_type',
    )
    search_fields = (
        'title',
    )
    inlines = [SlideInline]
    form = MaterialForm


admin.site.register(Material, MaterialAdmin)
