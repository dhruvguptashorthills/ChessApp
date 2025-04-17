from django.urls import path
from . import views
from django.conf import settings
from game.views import signup_view
from django.conf.urls.static import static

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('create-room/', views.create_room, name='create_room'),
    path('join-room/', views.join_room, name='join_room'),
    path('game/<str:room_id>/', views.play_game, name='play_game'),
    path('accounts/signup/', signup_view, name='signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
