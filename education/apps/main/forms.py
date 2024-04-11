from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Material, Slide


class MaterialForm(forms.ModelForm):

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


class SlideAdminForm(forms.ModelForm):

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
