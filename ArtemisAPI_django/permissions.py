from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated

from apps.users.models import User


class isAuthenticated(IsAuthenticated):
    """
    Grants access to authenticated users
    """

    def has_permission(self, request, view):

        is_authenticated = bool(request.user and request.user.is_authenticated)

        if is_authenticated:
            if request.method not in SAFE_METHODS:  # If request is something dangerous, check that the user is an admin
                has_permission = request.user.groups.filter(name='admins').exists()
                return has_permission

            has_permission = True
            return has_permission

        else:
            has_permission = False
            return has_permission


class isStudent(BasePermission):
    """
    Grants access to students
    """

    def has_permission(self, request, view):
        has_permission = request.user.groups.filter(name='students').exists()
        return has_permission


class isTeacher(BasePermission):
    """
    Grants access to teachers
    """

    def has_permission(self, request, view):
        has_permission = request.user.groups.filter(name='teachers').exists()
        return has_permission


class isAdmin(BasePermission):
    """
    Grants access to administrators
    """

    def has_permission(self, request, view):
        has_permission = request.user.groups.filter(name='admins').exists()
        return has_permission
