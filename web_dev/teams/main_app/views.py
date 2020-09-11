from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Count

from .models import Team, Player


class IndexView(View):
    def get(self, request):
        teams = Team.objects.all().annotate(player_count=Count('players')).order_by('location', 'name')
        context = {
            'all_teams' : teams,
        }

        return render(request, 'index.html', context)


class TeamView(View):
    def get(self, request, team_id):

        team = Team.objects.get(id=team_id)
        players = Player.objects.filter(team=team)
        context = {
            'team': team,
            'all_players' : players
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

class AddPlayerView(View):
    def post(self, request, team_id):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            team = Team.objects.get(id=team_id)
            print("Player created")
        except Team.DoesNotExist:
            print("Team doesn\'t exist")

            return redirect(f'/teams/{team_id}/')

        Player.objects.create(first_name=first_name, last_name=last_name, team=team)

        return redirect(f'/teams/{team_id}/')

class DeletePlayerView(View):
    def get(self, request, player_id, team_id):
        player = Player.objects.get(id=player_id)
        player.delete()

        return redirect(f'/teams/{team_id}')
