from django.test import TestCase
from django.utils.timezone import now
from django.urls import reverse

from datetime import timedelta

from .models import Question


def create_question(question_text, days):
    time = now() + timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


# Create your tests here.
class ModelQuestionTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = now() + timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = now() - timedelta(hours=23, minutes=59, seconds=59, milliseconds=99)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_old_question(self):
        time = now() - timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls available")
        self.assertQuerySetEqual(response.context["latest_questions_list"], [])

    def test_past_question(self):
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_questions_list"],
            [question],
        )

    def test_future_question(self):
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls available")
        self.assertQuerySetEqual(response.context["latest_questions_list"], [])

    def test_future_and_past_questions(self):
        question = create_question(question_text="Past question", days=-30)
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_questions_list"],
            [question],
        )

    def test_two_past_questions(self):
        question1 = create_question(question_text="Past question 1", days=-30)
        question2 = create_question(question_text="Past question 2", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_questions_list"],
            [question2, question1],
        )
