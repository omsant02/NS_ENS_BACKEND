from rest_framework import serializers
from .models import Friendship

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['id', 'from_ens', 'to_ens', 'created_at']
        read_only_fields = ['id', 'created_at']