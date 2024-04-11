from django.urls import path

from .views import MaterialDetailView, MaterialListView, TypeMaterialListView

urlpatterns = [
    path('', MaterialListView.as_view(), name='list'),
    path('types/<str:slug>', TypeMaterialListView.as_view(), name='material-type'),
    path('materials/<str:type>/<str:slug>', MaterialDetailView.as_view(), name='detail-material'),
]
