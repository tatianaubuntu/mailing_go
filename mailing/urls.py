from django.urls import path

from mailing.apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [
    # path('', BoatListView.as_view(), name='boat_list'),
    # path('<int:pk>/', BoatDetailView.as_view(), name='boat_detail'),
    ]
