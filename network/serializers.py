from rest_framework import serializers
from .models import NetworkNode


class NetworkNodeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели 'NetworkNode'. Закрываем для доступа по API возможность изменения задолженности."""

    class Meta:
        model = NetworkNode
        fields = '__all__'
        extra_kwargs = {
            'debt': {'read_only': True}
        }
