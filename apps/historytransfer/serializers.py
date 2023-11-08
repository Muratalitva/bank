from rest_framework import serializers
from apps.historytransfer.models import HistoryTransfer

class HistoryTransferSerializers(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = ('id', 'from_user', 'to_user', 'is_complated', 'created_at', 'amount')