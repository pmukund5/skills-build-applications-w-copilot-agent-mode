from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        print('Creating test users...')
        # Create test users
        user1 = User.objects.create(email='user1@example.com', name='User One', age=20)
        user2 = User.objects.create(email='user2@example.com', name='User Two', age=25)

        print('Creating test teams...')
        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        print('Creating test activities...')
        # Create test activities
        Activity.objects.create(user=user1, type='Running', duration=30)
        Activity.objects.create(user=user2, type='Cycling', duration=45)

        print('Creating test leaderboard entries...')
        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, points=100)
        Leaderboard.objects.create(user=user2, points=150)

        print('Creating test workouts...')
        # Create test workouts
        Workout.objects.create(name='Workout A', description='Description for Workout A')
        Workout.objects.create(name='Workout B', description='Description for Workout B')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
