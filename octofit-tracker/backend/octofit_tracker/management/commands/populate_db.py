
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with MonaFit-style test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        # Support both djongo legacy and CLIENT dict config
        db_settings = settings.DATABASES['default']
        if 'CLIENT' in db_settings:
            host = db_settings['CLIENT'].get('host', 'localhost')
            port = db_settings['CLIENT'].get('port', 27017)
        else:
            host = db_settings.get('HOST', 'localhost')
            port = db_settings.get('PORT', 27017)
        client = MongoClient(host, int(port))
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.user.drop()
        db.team.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workout.drop()

        # Create users
        users = [
            User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(_id=ObjectId(), username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(_id=ObjectId(), username='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
            User(_id=ObjectId(), username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        blue_team = Team(_id=ObjectId(), name='Blue Team')
        blue_team.save()
        for user in users:
            blue_team.members.add(user)

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=60),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=120),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=90),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=30),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], points=100),
            Leaderboard(_id=ObjectId(), user=users[1], points=90),
            Leaderboard(_id=ObjectId(), user=users[2], points=95),
            Leaderboard(_id=ObjectId(), user=users[3], points=85),
            Leaderboard(_id=ObjectId(), user=users[4], points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with MonaFit-style test data.'))
