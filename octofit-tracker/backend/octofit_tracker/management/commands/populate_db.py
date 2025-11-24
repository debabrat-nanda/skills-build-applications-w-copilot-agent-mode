
from django.core.management.base import BaseCommand
from pymongo import MongoClient
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboards.delete_many({})
        db.workouts.delete_many({})

        # Create teams
        marvel_id = db.teams.insert_one({"name": "marvel", "description": "Marvel Superheroes"}).inserted_id
        dc_id = db.teams.insert_one({"name": "dc", "description": "DC Superheroes"}).inserted_id

        # Create users
        users = [
            {"email": "ironman@marvel.com", "name": "Iron Man", "team": "marvel", "is_superhero": True},
            {"email": "captain@marvel.com", "name": "Captain America", "team": "marvel", "is_superhero": True},
            {"email": "batman@dc.com", "name": "Batman", "team": "dc", "is_superhero": True},
            {"email": "superman@dc.com", "name": "Superman", "team": "dc", "is_superhero": True},
        ]
        user_ids = db.users.insert_many(users).inserted_ids

        # Create activities
        activities = [
            {"user_id": user_ids[0], "type": "run", "duration": 30, "date": "2025-11-24"},
            {"user_id": user_ids[1], "type": "swim", "duration": 45, "date": "2025-11-23"},
            {"user_id": user_ids[2], "type": "cycle", "duration": 60, "date": "2025-11-22"},
            {"user_id": user_ids[3], "type": "yoga", "duration": 20, "date": "2025-11-21"},
        ]
        db.activities.insert_many(activities)

        # Create leaderboard
        db.leaderboards.insert_many([
            {"team_id": marvel_id, "points": 100},
            {"team_id": dc_id, "points": 80},
        ])

        # Create workouts
        db.workouts.insert_many([
            {"name": "Pushups", "description": "Do 20 pushups", "suggested_for": "marvel"},
            {"name": "Situps", "description": "Do 30 situps", "suggested_for": "dc"},
        ])

        # Ensure unique index on email field in users collection
        db.users.create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
