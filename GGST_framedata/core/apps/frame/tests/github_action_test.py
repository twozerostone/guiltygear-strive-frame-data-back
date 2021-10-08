from django.test import TestCase


class GithubActionTest(TestCase):
    def test_github_hello(self):
        self.assertEqual('hello github test', 'hello github test')
