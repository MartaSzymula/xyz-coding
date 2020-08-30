from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from .models import User

# Create your views here.

class CreateUserView(View):

    def get(self, request):
        User.objects.create(first_name='Fred', last_name='Random', email='random@hogwarts.com')

        return HttpResponse('Complete')

class GetUsersView(View):
    def get(self, request):
        all_users = User.objects.all()
        for user in all_users:
            print(user)

        # FILTERING
        # freds = User.objects.filter(first_name='Fred')
        # for f in freds:
        #     print(f)
        #
        # GET
        # get_user = User.objects.get(id=1)
        # print(get_user)

        return HttpResponse('Got all users')

class UpdateUsersView(View):
    def get(self, request):
        # User.objects.filter(id=3).update(first_name='George')

        user = User.objects.get(id=3)
        user.last_name = 'Weasley'
        user.save()

        return redirect('/read/')

class DeleteUsersView(View):
    def get(self, request):
        User.objects.get(id=2).delete()

        return redirect('/read/')


# def index(request):
#     if 'counter' in request.session:
#         request.session['counter'] += 1
#     else:
#         request.session = 1
#
#     return render(request, 'index.html')

class login_view(View):
    def get(self, request):

        return render(request, 'index.html')

    def post(self, request):


        print("Email is: ")
        print(request.POST.get('email'))
        # get('must_match_name in html')
        return redirect('/')

class reddit_view(View):
    def get(self, request, page_name):
        context = {
        'page_name': page_name
        }
        return render(request, 'page.html', context)

# def page(request, page_name):


def countries(request):
    countries = ['France', 'Portugal', 'the Netherlands', 'Spain', 'United Kingdom']
    context = {
        'all_countries': countries
    }

    return render(request, 'countries.html', context)

def states(request):
    states = [
    {'name': 'California', 'abbr': 'CA'},
    {'name': 'Washington', 'abbr': 'WA'},
    {'name': 'Ney York', 'abbr': 'NY'}

    ]

    context = {
        'all_states': states
    }

    return render(request, 'states.html', context)
