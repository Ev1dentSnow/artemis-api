from rest_framework.permissions import BasePermission

from apps.users.models import User


class isStudent(BasePermission):
    """
    Grants access to students
    """

    def has_permission(self, request, view):
        user_id = request.user.id
        role = request.user.role
        has_permission = User.objects.filter(id=user_id, role=role).exists()
        return has_permission


class isTeacher(BasePermission):
    """
    Grants access to teachers
    """

    def has_permission(self, request, view):
        user_id = request.user.id
        role = request.user.role
        has_permission = User.objects.filter(id=user_id, role=role).exists()
        return has_permission


class isAdmin(BasePermission):
    """
    Grants access to administrators
    """

    def has_permission(self, request, view):
        user_id = request.user.id
        role = request.user.role
        has_permission = User.objects.filter(id=user_id, role=role).exists()
        return has_permission
