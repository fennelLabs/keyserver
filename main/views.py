from main.models import UserKeys
from main.serializers import UserKeysSerializer
from rest_framework import viewsets
import django_filters.rest_framework


class UserKeysViewSet(viewsets.ModelViewSet):
    queryset = UserKeys.objects.all()
    serializer_class = UserKeysSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        queryset = UserKeys.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset
