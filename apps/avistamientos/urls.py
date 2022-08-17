from django.urls import path
from .views import AvistamientosList,AvistamientosDestroy,AvistamientosUpdate,avistamientoForIdEspecie,list_marine_OIH,findid

urlpatterns = [
    path('avistamientos/', AvistamientosList.as_view(), name='avistamientos-list'),
    path('avistamientos/destroy/<int:pk>/', AvistamientosDestroy.as_view(), name='avistamientos-destroy'),
    path('avistamientos/update/<int:pk>/', AvistamientosUpdate.as_view(), name='avistamientos-update'),
    # categoria for id especie
    path('findavistamiento/<int:pk>/', avistamientoForIdEspecie.as_view(), name='avistamientoForIdEspecie'),
    
    
    # old
    path('chm/api/oih/',list_marine_OIH, name='OIH Metadata Expose'),

    # new
    path('chm/api/oih/findid/<str:categoria>/<str:id>',  findid, name='list_origin'),
]
