import json
import scrapy
from ..items import ArticleItem
from datetime import datetime, date

# DATE = datetime.date(datetime.now())
DATE = date(2020, 8, 1)


class NewsSpider(scrapy.Spider):
    name = 'news'
    page = 1
    start_urls = [
        'https://www.grammarly.com/blog/wp-json/grammarly/contenthub/posts/?page=1']

    def parse(self, response):
        data = json.loads(response.text)

        for article in data:
            dt = datetime.strptime(article['date'], "%Y-%m-%dT%H:%M:%S")
            if dt.date() >= DATE:
                item = ArticleItem()
                item['title'] = article['title']['rendered']
                item['content'] = article['content']['rendered']
                item['date_posted'] = article['date']
                item['origin_link'] = article['link']
                yield item
            else:
                return

        self.page += 1
        url = 'https://www.grammarly.com/blog/wp-json/grammarly/contenthub/posts/?page={}'.format(
            self.page)
        yield response.follow(url=url, callback=self.parse)
