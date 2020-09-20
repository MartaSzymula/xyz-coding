from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages

class IndexView(View):
    def get(self, request):

        return render(request, 'index.html')

class RegistrationView(View):
    def post(self, request):

        is_valid = True

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # print(len(first_name))

        if len(first_name) < 2:
            is_valid = False
            messages.error(request, 'first_name must be at least 2 characters.')

        if len(last_name) < 2:
            is_valid = False
            messages.error(request, 'last_name must be at least 2 characters.')


        if len(username) < 6:
            is_valid = False
            messages.error(request, 'username must be at least 6 characters.')

        if len(email) < 6:
            is_valid = False
            messages.error(request, 'email must be at least 6 characters.')

        if len(password) < 8:
            is_valid = False
            messages.error(request, 'password must be at least 8 characters.')

        if User.objects.filter(Q(username=username)|Q(email=email)):
            is_valid = False
            messages.error(request, 'This username/email already exists.')

        if is_valid==False:
            return redirect('/')

        else:
            user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
            )

            print("Hashed password")
            print(user.password)

            return redirect('/')
