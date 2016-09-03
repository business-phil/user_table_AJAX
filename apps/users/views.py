from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Q
from .models import User
from .forms import UserForm

class Users(View):
    def get(self, request):
        request.session.clear()
        userquery = User.objects.all()
        pagecount = int(float(len(userquery)-1)/5)
        context = {
            'users': userquery[0:5],
            'rowcount': range(len(userquery), 5),
            'pagerange': range(pagecount+1),
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
            request.session.clear()
        return redirect('filter')

class Filter(View):
    def get(self, request):
        userquery = User.objects.all()
        if 'filterargs' in request.session:
            if request.session['filterargs'][0]:
                userquery = userquery.filter(Q(first_name__contains=request.session['filterargs'][0]) | Q(last_name__contains=request.session['filterargs'][0]))
            if request.session['filterargs'][1]:
                userquery = userquery.filter(created_at__gte=request.session['filterargs'][1])
            if request.session['filterargs'][2]:
                userquery = userquery.filter(created_at__lte=request.session['filterargs'][2])
                # Does not include same day, since date input defaults to 00:00am
                # May need to isolate created_at date when comparing to date input
        querylimit = request.session['querylimit'] if 'querylimit' in request.session else (0, 5)
        pagecount = int(float(len(userquery)-1)/5)
        context = {
            'users': userquery[querylimit[0]:querylimit[1]],
            'rowcount': range(len(userquery[querylimit[0]:querylimit[1]]), 5),
            'pagerange': range(pagecount+1),
        }
        return render(request, 'users/index_table.html', context)

    def post(self, request):
        start = 5*(int(request.POST['page'])-1)
        end = start + 5
        request.session['filterargs'] = (request.POST['name'], request.POST['date_from'], request.POST['date_to'])
        request.session['querylimit'] = (start, end)
        return redirect('filter')
