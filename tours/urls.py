from django import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
        path('', ListView.as_view(), name='tour_list'),
        path('<int:pk>/', DetailView.as_view(), name='tour_detail'),
        path('create/', CreateView.as_view(), name ='create_tour'),
        path('update/<int:pk>/', UpdateView.as_view(), name='update_tour'),
        path('delete/<int:pk>/', DeleteView.as_view(), name='delete_tour'),
]
