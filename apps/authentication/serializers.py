from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        roles = []
        groups = user.groups.all()

        for group in groups:
            roles.append(group.name)

        token['roles'] = roles
        return token
