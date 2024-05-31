from django.urls import path

from client.apps import ClientConfig
from client.views import ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView, ClientCreateView

app_name = ClientConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
]

