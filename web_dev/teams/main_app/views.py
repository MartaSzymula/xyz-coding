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
        print(request.POST)

        return redirect('/teams/')
