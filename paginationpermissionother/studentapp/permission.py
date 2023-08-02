from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and str(request.user.user_type) == 'AD' or request.user.is_superuser or str(request.user.user_type) == 'EMP')