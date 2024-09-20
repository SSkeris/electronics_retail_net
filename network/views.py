from rest_framework import viewsets, permissions
from .models import NetworkNode
from .serializers import NetworkNodeSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """Представление модели 'NetworkNode'."""
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Фильтр для запроса по параметру 'country'."""

        queryset = NetworkNode.objects.all()
        country = self.request.query_params.get('country', None)
        if country is not None:
            queryset = queryset.filter(contact__country=country)
        return queryset
