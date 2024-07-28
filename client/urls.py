from django.urls import path

from client.apps import ClientConfig
from client.views import (ClientListView, ClientDetailView, ClientUpdateView,
                          ClientDeleteView, ClientCreateView, StatisticTemplateView)

app_name = ClientConfig.name

urlpatterns = [
    path('', StatisticTemplateView.as_view(), name='statistic'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
]
