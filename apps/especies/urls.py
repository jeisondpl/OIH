from django.urls import path
from .views import EspecieList, CategoriaList, EspecieDestroy, EspecieUpdate,CategoriaDestroy, CategoriaUpdate

urlpatterns = [
    # especies
    path('especies/', EspecieList.as_view(), name='especie-list'),
    path('especies/destroy/<int:pk>/', EspecieDestroy.as_view(), name='especie-destroy'),
    path('especies/update/<int:pk>/', EspecieUpdate.as_view(), name='especie-update'),
    # categoria
    path('categoria/', CategoriaList.as_view(), name='categoria-list'),
    path('categoria/destroy/<int:pk>/', CategoriaDestroy.as_view(), name='categoria-destroy'),
    path('categoria/update/<int:pk>/', CategoriaUpdate.as_view(), name='categoria-update'),

]
