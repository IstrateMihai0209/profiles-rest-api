from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    #Allow user to update only their own profile

    def has_object_permission(self, request, view, obj):
        #Check if the user is trying to edit their own profile

        # If the method is safe, like GET, the user is allowed to read the data
        if request.method in permissions.SAFE_METHODS:
            return True
        # The user is allowed to use any HTTP method only if it's his own profile
        return obj.id == request.user.id
