from django.urls import path
from . views import overall, MatchDetailView


urlpatterns = [
    path('', overall, name='goals'),
    path('match/<int:day>_<int:month>_<int:year>/', MatchDetailView.as_view(), name='match-detail'),
]