from django.test import TestCase

from project.judge.models import ParentScoreCategory
from project.judge.models import ScoreCategory
from project.judge.models import ScoreMetric
from project.judge.models import Level
from project.judge.models import Team
from project.judge.models import Round
from project.judge.models import Championship


# Create your tests here.


class ParentScoreCategoryModelTest(TestCase):

    def test_string_representation(self):
        parent_score_category = ParentScoreCategory(name="name of a parent score category")
        self.assertEqual(str(parent_score_category), parent_score_category.name)


class ScoreCategoryModelTest(TestCase):

    def test_string_representation(self):
        score_category = ScoreCategory(name="name of a score category")
        self.assertEqual(str(score_category), score_category.name)

class ScoreMetricModelTest(TestCase):

    def test_string_representation(self):
        score_metric = ScoreMetric(name="name of a score metric")
        self.assertEqual(str(score_metric), score_metric.name)

class LevelModelTest(TestCase):
    
    def test_string_representation(self):
        level = Level(name="name of a level")
        self.assertEqual(str(level), level.name)

class TeamModelTest(TestCase):

    def test_string_representation(self):
        team = Team(name="name of a team")
        self.assertEqual(str(team), team.name)

class RoundModelTest(TestCase):

    def test_string_representation(self):
        round = Round(name="name of a round")
        self.assertEqual(str(round), round.name)

class ChampionshipModelTest(TestCase):

    def test_string_representation(self):
        championship = Championship(name="name of a championship")
        self.assertEqual(str(champion), championship.name)