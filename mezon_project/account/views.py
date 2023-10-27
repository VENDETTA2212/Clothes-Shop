from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.views import View


class RegisterLoginView(View):
    def get(self, request:WSGIRequest):
        if request.user.is_anonymous:
            print('anonymous')
            return render(request, 'account/login_register.html')
        elif request.user.is_authenticated:
            print('authenticated')
            return render(request, 'account/user_profile.html')
    
    def post(self, request:WSGIRequest):
        if request.POST.get('Action') == 'Login':
            print('login')
        elif request.POST.get('Action') == 'Register':
            print('Register')
        else:
            return render(request, 'account/LoginRegister.html')
        print(request.user)
        return render(request, 'account/LoginRegister.html')
    

class HomeView(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass
