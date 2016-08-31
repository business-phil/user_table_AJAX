from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.views.generic import View

class Users(View):
    def get(self, request):
        userquery = User.objects.all()
        context = {
            'users': userquery,
            'add_user': UserForm(),
        }
        return render(request, 'users/index.html', context)

    def post(self, request):
        create_form = UserForm(request.POST)
        if create_form.is_valid():
            fName = request.POST['first_name']
            lName = request.POST['last_name']
            email = request.POST['email']
            User.objects.create(first_name=fName, last_name=lName, email=email)
        return redirect('index')

class Filter(View):
    def post(self, request)
