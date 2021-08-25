import re

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
                has_permission = False
                return has_permission

            has_permission = True
            return has_permission

        else:
            has_permission = False
            return has_permission


class isOwner(BasePermission):
    """
    Grants access if the requested resource 'belongs' to the user. e.g if a student is trying to access their marks, or their class's info
    This disallows some other student from viewing this requested students data, however with the help of the other permissions, teachers
    and or admins will still be able to override this permission as they need to view data for all students and not just one
    """

    def has_permission(self, request, view):
        we = request._request.path
        requested_id = 0

        for word in we.split("/"):
            if word.isdigit():
                requested_id = word
                break

        if request.user.id == requested_id:
            has_permission = True
            return has_permission
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
