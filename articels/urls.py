from django.urls import path
from . import views
app_name = 'articels'
urlpatterns = [
    path('', views.articel_list, name='list'),
    path('create', views.articel_create, name='create'),
    path('<slug>',views.articel_detail, name='detail'),
]
