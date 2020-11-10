from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect

class UserAccessMixin(PermissionRequiredMixin):
    redirect_without_permission = None
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(),
                                     self.get_login_url(), self.get_redirect_field_name())
        
        if(not self.has_permission()):
            return redirect(self.redirect_without_permission)
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)