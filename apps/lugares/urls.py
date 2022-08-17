from django.urls import path
from .views import LugaresList,LugaresDestroy,LugaresUpdate

urlpatterns = [
    path('lugares/', LugaresList.as_view(), name='lugares-list'),
    path('lugares/destroy/<int:pk>/', LugaresDestroy.as_view(), name='lugares-destroy'),
    path('lugares/update/<int:pk>/', LugaresUpdate.as_view(), name='lugares-update'),

]
