import re

from django.db.models import Q
from django.views import generic

from .models import Material


class MaterialListView(generic.ListView):
    queryset = Material.objects.all()
    context_object_name = 'materials'
    template_name = 'main/list.html'
    extra_context = {'title': 'Главная', 'types': Material.Type.choices}
    
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            filters = Q()
            for word in re.split(r"[,\s]", query):
                filters |= Q(key_words__icontains=word)
            return self.queryset.filter(filters)
        return super(MaterialListView, self).get_queryset()


class MaterialDetailView(generic.DetailView):
    queryset = Material.objects.all()
    slug_url_kwarg = 'slug'
    context_object_name = 'material'
    template_name = 'main/detail.html'

    def get_queryset(self):
        return Material.objects.filter(material_type=self.kwargs.get('type'))


class TypeMaterialListView(MaterialListView):

    def get_queryset(self):
        return Material.objects.filter(material_type=self.kwargs.get('slug'))


# class SearchView(generic.ListView):
#     context_object_name = 'materials'
#     template_name = 'main/list.html'
#     extra_context = {'title': 'Главная', 'types': Material.Type.choices}
