from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.views.generic import View

class Index(View):
    def get(self, request):
        userquery = User.objects.all()
        context = {
            'users': userquery,
            'add_user': UserForm(),
        }
        return render(request, 'users/index.html', context)

    def post(self, request):
        return redirect('index')

class Create(View):
    def post(self, request):
        return redirect('index')
