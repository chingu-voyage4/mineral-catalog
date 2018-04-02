from django.test import TestCase
from django.urls import reverse

from .models import Mineral, Group, Category


class MineralModelTests(TestCase):

    def setUp(self):
        self.new_mineral = Mineral.objects.create(name='Test')
        self.new_mineral.save()

    def test_name(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

class IndexViewTests(TestCase):
    def test_future_question_and_past_question(self):

        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )