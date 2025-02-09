from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    IntegerField,
    ForeignKey,
    CASCADE,
)
from django.utils.timezone import now
from datetime import timedelta


class Question(Model):
    question_text = CharField(max_length=200)
    pub_date = DateTimeField("date published")

    def was_published_recently(self):
        return now() - timedelta(days=1) <= self.pub_date <= now()

    def __str__(self):
        return self.question_text


class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    choice_text = CharField(max_length=30)
    votes = IntegerField(default=0)

    def __str__(self):
        return self.choice_text
