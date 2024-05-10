from django.shortcuts import render
from django.db.models import Count, Case, When, IntegerField, Sum, F
from django.views.generic import DetailView
from .models import Player, Goal, Match
from django.db import models
from django.shortcuts import get_object_or_404


def overall(request):
    player_goals = Player.objects.annotate(
        total_goals=Sum('goal__goals_scored'),
        matches_played=Count('goal__match', distinct=True)
    ).order_by('-total_goals', '-matches_played')

    matches = Match.objects.annotate(total_goals=Sum('goal__goals_scored'))

    total_goals_all_matches = Goal.objects.aggregate(total_goals=Sum('goals_scored'))['total_goals']
    total_counter_goals_all_matches = Match.objects.aggregate(total_counter_goals=Sum('counter_goals'))['total_counter_goals']
    goal_difference = total_goals_all_matches - total_counter_goals_all_matches

    # Calculate total wins and losses for the team
    wins_losses = matches.annotate(
        outcome=Case(
            When(total_goals__gt=F('counter_goals'), then=1),
            When(total_goals__lt=F('counter_goals'), then=-1),
            default=0,
            output_field=IntegerField(),
        )
    ).aggregate(
        total_wins=Count(Case(When(outcome=1, then=1), output_field=IntegerField())),
        total_losses=Count(Case(When(outcome=-1, then=1), output_field=IntegerField()))
    )

    return render(request, 'goal/main.html', {
        'top_scorers': player_goals, 
        'matches': matches, 
        'goal_difference': goal_difference,
        'total_goals': total_goals_all_matches,
        'total_counter_goals': total_counter_goals_all_matches,
        'total_wins': wins_losses['total_wins'],
        'total_losses': wins_losses['total_losses'],
        })

class MatchDetailView(DetailView):
    model = Match
    template_name = 'goal/match.html'

    def get_object(self, queryset=None):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        return get_object_or_404(Match, date__year=year, date__month=month, date__day=day)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        match = self.get_object()
        
        # Get all goals for the match
        match_goals = Goal.objects.filter(match=match)
        total_goals = match_goals.aggregate(total_goals=Sum('goals_scored'))['total_goals']

        # Count goals for each player in the match
        player_goals_count = match_goals.values('player__name').annotate(total_goals=models.Count('id'))

        context['match_goals'] = match_goals
        context['player_goals_count'] = player_goals_count
        context['total_goals'] = total_goals
        return context
