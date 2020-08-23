from scrapy_djangoitem import DjangoItem
from news.models import Article


class ArticleItem(DjangoItem):
    django_model = Article
