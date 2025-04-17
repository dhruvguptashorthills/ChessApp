# Generated by Django 5.2 on 2025-04-15 09:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fen', models.CharField(default='startpos', help_text='Current board position in Forsyth-Edwards Notation', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('player_black', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='black_games', to=settings.AUTH_USER_MODEL)),
                ('player_white', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='white_games', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
