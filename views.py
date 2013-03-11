from django.template import Context, loader
from rostermaker.models import Player
from django.http import HttpResponse


def players(request):
    players_list = Player.objects.all().order_by('lastName', 'firstName')
    count = len(players_list)
    t = loader.get_template('players.html')
    c = Context({
        'players_list': players_list,
        'count': count,
    })
    return HttpResponse(t.render(c))