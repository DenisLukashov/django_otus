from datetime import date

from django.test import TestCase
from playground.models import Article, Publisher


class ArticleTestCase(TestCase):

    recently_added_article = 'recently_added_article'
    an_old_article = 'an_old_article'

    def test_added_recently_true(self):
        article = Article(
            title=self.recently_added_article,
            pub_date=date.today(),
        )
        self.assertTrue(article.added_recently)

    def test_added_recently_false(self):
        article = Article(
            title=self.an_old_article,
            pub_date=date(2019, 1, 13),
        )
        self.assertFalse(article.added_recently)


class PlaygroundViewTestCase(TestCase):

    def setUp(self):
        publisher = Publisher.objects.create(
            first_name='J',
            last_name='S',
            email='j@s.com',
        )

        for title in map(str, range(100)):
            Article.objects.create(
                title=title,
                pub_date=date.today(),
                publisher=publisher,
            )

    def test_index_context(self):
        response = self.client.get('/playground/')
        articles = [a for a in response.context['articles']]
        expected_articles = [a for a in Article.objects.all()]
        self.assertEqual(articles, expected_articles)
