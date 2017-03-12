
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scraper.items import ScraperItem


class FirstCrawl(CrawlSpider):
    name = 'simplecrawl'
    allowed_domains = ["wiprodigital.com"]
    start_urls = ["http://wiprodigital.com/"]

    rules = (Rule(LinkExtractor(allow=()), callback='parse_items', follow=True),)

    def parse_items(self, response):

        crawlpages = response.xpath('//div')
        items = []

        for pageinfo in crawlpages:
            item = ScraperItem()
            item['link'] = pageinfo.select("a/@href").extract()
            item['imageLink'] = pageinfo.select("a//img/@src").extract()
            if item['link'] or item['imageLink']:
                items.append(item)
        for item in items:
                yield item


