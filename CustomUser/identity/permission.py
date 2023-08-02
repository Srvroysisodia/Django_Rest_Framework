'''This file contains the code to provide permissions to the user as per the method'''
# import the function 
from rest_framework import permissions


# Cresting a class to give permissions based on user action 
class ActionBasedPermissions(permissions.BasePermission):
    ''' 
    Grand or deny access to a view , based on mapping in view .action_permissions
    '''
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and str(request.user.is_approve)== 'True' and str(request.user.user_profile) == 'Teacher' or request.user.is_superuser or str(request.user.user_profile) == 'Admin')


        # '''This file contains the code to provide permissions to the user as per the method'''
class UserBasedPermissions(permissions.IsAuthenticated):
    '''
     Grand or deny access to a view , based on mapping in view .action_permissions'''
    def has_permission(self, request, view):
        '''
         Function to set permission as per the request method
         '''
        for cls , action in getattr(view,'action_permissions',{}).items():
             if view.action in action:
                 return cls().has_permission(request,view)
        return False

# Cresting a class to give permissions based on user action 
class DeleteBasedPermissions(permissions.BasePermission):
    ''' 
    Grand or deny access to a view , based on mapping in view .action_permissions
    '''

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser or str(request.user.user_profile) == 'Admin' and str(request.user.is_approve)== 'True')

class IsCreatorOrAdmin(permissions.BasePermission):
    """
    Check if authenticated user is seller of the product or admin
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated is True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.created_by == request.user or str(request.user.user_profile) == 'Admin'