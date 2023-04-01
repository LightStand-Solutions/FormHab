from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import mixins, GenericViewSet
from apps.user.serializers import TokenCustomSerializer


class CreateUsers(mixins.CreateModelMixin, GenericViewSet):
    def create(self, request, *args, **kwargs):
        return 'aaa'


class TokenCustomView(TokenObtainPairView):
    serializer_class = TokenCustomSerializer

