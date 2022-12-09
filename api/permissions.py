from rest_framework import permissions

# Custom permission to only allow owners of an object to edit it.

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):            # Read permissions are allowed to any request,              
        if request.method in permissions.SAFE_METHODS:              # so we'll always allow GET, HEAD or OPTIONS requests.
            return True       
        return obj.owner == request.user                            # Write permissions are only allowed to the owner of the reminder.
