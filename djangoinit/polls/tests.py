from django.test import TestCase
from django.utils.timezone import now

from datetime import timedelta

from .models import Question


# Create your tests here.
class ModelQuestionTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = now() + timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = now() - timedelta(hours=12)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_old_question(self):
        time = now() - timedelta(days=2)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
