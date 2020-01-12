from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to update own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user trying to update their own profile"""
        #  We want all users allow to view everyones profiles So permissions.SAFE_METHODS used
        # But dont allow to edit or delete
        if request.method in permissions.SAFE_METHODS:
            #This safe method is Get method
            return True

        # But if logged in user wants to edit own profile then allow her/him
        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """Allow user to update their own feed status"""
    def has_object_permission(self, request, view, obj):
        """Check user trying to update their own status"""
        #  We want all users allow to view everyones profiles So permissions.SAFE_METHODS used
        # But dont allow to edit or delete
        if request.method in permissions.SAFE_METHODS:
            #This safe method is Get method
            return True

        # But if logged in user wants to edit own profile then allow her/him
        return obj.user_profile.id == request.user.id
