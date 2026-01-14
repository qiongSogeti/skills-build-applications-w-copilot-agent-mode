from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='TestTeam')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team='TestTeam')
        self.activity = Activity.objects.create(name='TestActivity', user=self.user, team=self.team)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=50)
        self.workout = Workout.objects.create(name='TestWorkout', description='TestDesc')

    def test_user(self):
        self.assertEqual(self.user.email, 'test@example.com')

    def test_team(self):
        self.assertEqual(self.team.name, 'TestTeam')

    def test_activity(self):
        self.assertEqual(self.activity.name, 'TestActivity')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 50)

    def test_workout(self):
        self.assertEqual(self.workout.name, 'TestWorkout')
