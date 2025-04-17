import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Game
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


def lobby(request):
    return render(request, 'game/lobby.html')
@login_required
def create_room(request):
    room_id = str(uuid.uuid4())[:8]  # Short unique ID
    # Save to DB with current user as white
    Game.objects.create(
        id=room_id,
        player_white=request.user
    )
    return redirect('play_game', room_id=room_id)
@login_required
def join_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        return redirect('play_game', room_id=room_id)
    return redirect('lobby')

@login_required
def play_game(request, room_id):
    game = Game.objects.filter(id=room_id).first()

    if not game:
        return render(request, 'game/invalid_room.html', {'room_id': room_id})

    if game.player_black is None and game.player_white != request.user:
        game.player_black = request.user
        game.save()

    color = game.get_player_color(request.user)

    return render(request, 'game/board.html', {
        'room_id': room_id,
        'username': request.user.username,
        'color': color
    })

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
