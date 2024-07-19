from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from gamestore.forms import GameForm
from gamestore.models import Game


def index(request):
    return render(request, 'gamestore/index.html')

class GameListView(ListView):
    model = Game
    template_name = 'gamestore/game_list.html'
    context_object_name = 'games'

class GameDetailView(DetailView):
    model = Game
    template_name = 'gamestore/game_detail.html'

class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'gamestore/game_form.html'

class GameUpdateView(UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'gamestore/game_form.html'

class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy('game-list')
    template_name = 'gamestore/game_confirm_delete.html'
