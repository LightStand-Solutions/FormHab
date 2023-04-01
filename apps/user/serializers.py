from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenCustomSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        print(data)

        data['id'] = self.user.id
        data['username'] = self.user.username
        data['isSuperUser'] = self.user.is_superuser

        return data
