from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Team


class IndexView(View):
    def get(self, request):
        teams = Team.objects.all()
        context = {
            'all_teams' : teams,
        }

        return render(request, 'index.html', context)


class TeamView(View):
    def get(self, request, team_id):

        team = Team.objects.get(id=team_id)
        print(team)
        context = {
            'team': team,
        }
        return render(request, 'team.html', context)


class CreateTeamView(View):
    def get(self, request):

        return render(request, 'create.html')

    def post(self,request):
        new_name = request.POST.get('name')
        new_location = request.POST.get('location')
        new_mascot = request.POST.get('mascot')

        Team.objects.create(name=new_name, location=new_location, mascot=new_mascot)

        return redirect('/')


class EditTeamView(View):
    def get(self, request, team_id):
        team = Team.objects.get(id=team_id)
        context = {
            'team' : team
        }

        return render(request, 'edit.html', context)

    def post(self, request, team_id):
        team = Team.objects.get(id=team_id)

        team.name = request.POST.get('name')
        team.location = request.POST.get('location')
        team.mascot = request.POST.get('mascot')

        team.save()

        return redirect(f'/teams/{team_id}/')

class DeleteTeamView(View):
    def get(self, request, team_id):
        team = Team.objects.get(id=team_id)
        team.delete()

        return redirect('/')
