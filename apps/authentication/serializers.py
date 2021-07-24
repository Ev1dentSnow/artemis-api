from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        roles = ''
        delimeter = ','

        if user.is_student:
            roles += 'student'

        elif user.is_teacher:
            roles += 'teacher'
            if user.is_staff or user.is_superuser:  # Some teachers are admins too
                roles = roles + delimeter + 'admin'

        if user.is_staff or user.is_superuser:  # Not all admins are teachers
            roles += 'admin'

        token['roles'] = roles
        return token
