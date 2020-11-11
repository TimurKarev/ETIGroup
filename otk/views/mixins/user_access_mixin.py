from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect

class UserAccessMixin(PermissionRequiredMixin):
    redirect_without_permission = None
    view_name = None

    def dispatch(self, request, *args, **kwargs):
        print('Class name = ', self.view_name)
        if(not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(),
                                     self.get_login_url(), self.get_redirect_field_name())
        
        if(not self.has_permission()):
            if(self.view_name is None):
                return redirect(self.redirect_without_permission)
            else:
                return redirect(self.view_name, pk = kwargs['pk'])
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)