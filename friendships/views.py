from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Friendship
from .serializers import FriendshipSerializer

class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
    
    def create(self, request, *args, **kwargs):
        """Create a new friendship"""
        from_ens = request.data.get('from_ens')
        to_ens = request.data.get('to_ens')
        
        # Validate inputs
        if not from_ens or not to_ens:
            return Response(
                {'error': 'Both from_ens and to_ens are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if friendship already exists (in either direction)
        exists = Friendship.objects.filter(
            from_ens=from_ens, to_ens=to_ens
        ).exists() or Friendship.objects.filter(
            from_ens=to_ens, to_ens=from_ens
        ).exists()
        
        if exists:
            return Response(
                {'error': 'Friendship already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create friendship
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)