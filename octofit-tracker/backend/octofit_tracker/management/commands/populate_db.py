from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        print('Creating test users...')
        user1 = User.objects.create(username='alice', email='alice@example.com', password='password123')
        user2 = User.objects.create(username='bob', email='bob@example.com', password='password456')

        print('Creating test teams...')
        team1 = Team.objects.create(name='Team Red')
        team2 = Team.objects.create(name='Team Blue')
        team1.members.add(user1)
        team2.members.add(user2)

        print('Creating test activities...')
        Activity.objects.create(user=user1, activity_type='Running', duration=30)
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45)

        print('Creating test leaderboard entries...')
        Leaderboard.objects.create(user=user1, points=120)
        Leaderboard.objects.create(user=user2, points=150)

        print('Creating test workouts...')
        Workout.objects.create(name='Cardio Blast', description='A high-intensity cardio workout')
        Workout.objects.create(name='Strength Builder', description='A workout focused on strength training')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
