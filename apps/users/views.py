from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Q
from .models import User
from .forms import UserForm

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
        return redirect('filter')

class Filter(View):
    def get(self, request):
        userquery = User.objects.all()
        context = { 'users': userquery }
        return render(request, 'users/index_table.html', context)

    def post(self, request):
        userquery = User.objects.all()
        if request.POST['name']:
            userquery = userquery.filter(Q(first_name__contains=request.POST['name']) | Q(last_name__contains=request.POST['name']))
        if request.POST['date_from']:
            userquery = userquery.filter(created_at__gte=request.POST['date_from'])
        if request.POST['date_to']:
            userquery = userquery.filter(created_at__lte=request.POST['date_to'])
            # Does not include same day, since date input defaults to 00:00am
            # May need to exclude created_at time when comparing to date input
        context = { 'users': userquery[0:5], 'add_user': UserForm() }
        return render(request, 'users/index.html', context)
