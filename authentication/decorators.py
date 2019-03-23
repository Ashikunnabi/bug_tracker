from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied


def has_access(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            request.role = str(request.user.groups.all()[0])
            if request.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return wrap
    return decorator
