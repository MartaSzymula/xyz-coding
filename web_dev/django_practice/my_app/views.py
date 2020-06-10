from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session = 1

    return render(request, 'index.html')

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
