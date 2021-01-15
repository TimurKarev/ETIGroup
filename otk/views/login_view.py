import json

from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.http import JsonResponse


class LoginView(TemplateView):
    template_name = 'vue_login.html'

    def post(self, request, *args, **kwargs):

        post_data = json.loads(request.body)

        user = authenticate(
            username=post_data['login'],
            password=post_data['password'])

        response = 'error'
        if user is not None:
            if user.is_active:
                #print(request.POST)
                login(request=request, user=user)
                if user.is_authenticated:
                    response = 'ok'

        print(user)

        return JsonResponse({"message": response})