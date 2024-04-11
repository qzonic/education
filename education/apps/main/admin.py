from django.contrib import admin

from .models import Material, Slide
from .forms import MaterialForm, SlideAdminForm


class SlideInline(admin.TabularInline):
    model = Slide
    form = SlideAdminForm


class MaterialAdmin(admin.ModelAdmin):
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
