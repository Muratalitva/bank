from django.urls import path

from apps.historytransfer.views import CreateTransferView

urlpatterns = [
    path('transfer/', CreateTransferView.as_view(), name='transfer')
]