from rest_framework.permissions import BasePermission


class BaseFacilitiesPermission(BasePermission):

    def belongsToGroup(self, request, group):
        return request.user.groups.filter(name=group).exists()


class IsFacilitiesManager(BaseFacilitiesPermission):
    """
    Custom permission class to allow only facilities managers
    """

    def has_permission(self, request, view):
        """
        Return True if user is a facilities manager
        """
        return self.belongsToGroup(request, "FacilitiesAdmin")


class IsFinanceUser(BaseFacilitiesPermission):
    """
    Custom permission class to allow only finance dept users
    """

    def has_permission(self, request, view):
        """
        Return True if user is a finance dept user
        """
        return self.belongsToGroup(request, "Finance")


class IsPNCUser(BaseFacilitiesPermission):
    """
    Custom permission class to allow only PNC users
    """

    def has_permission(self, request, view):
        """
        Return True if user is a PNC user
        """
        return self.belongsToGroup(request, "PNC")


class IsFellow(BaseFacilitiesPermission):
    """
    Custom permission class to allow only fellows
    """

    def has_permission(self, request, view):
        """
        Return True if user is a fellow
        """
        return self.belongsToGroup(request, "Fellow")


class IsFellowOccupant(BaseFacilitiesPermission):
    """
    Custom permission class to allow only fellow occupant
    """

    def has_permission(self, request, view):
        """
        Return True if user is a fellow occupant
        """
        return self.belongsToGroup(request, "FellowOccupant")
