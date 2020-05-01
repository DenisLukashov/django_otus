from django.urls import path, register_converter
from . import views


app_name = 'homepage'


class YearConverter:
    regex = r'[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value


register_converter(YearConverter, 'year')


urlpatterns = [
    path(
        '',
        views.TemplateView.as_view(template_name='homepage/index.html'),
        name='index'
    ),
    path('articles/', views.ArticleView.as_view(), name='articles'),
    # re_path(
    #     r'^articles/(?P<year>[0-9]{4})/$',
    #     views.article_year, name='articles'
    # ),
    path('articles/<year:year>/', views.article_year, name='articles_year'),
]
