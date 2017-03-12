# import only subsets of the scrapy framework
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scraper.items import ScraperItem


class FirstCrawl(CrawlSpider):

    name = 'simplecrawl'

    # Challenge - allowed domain fulfils the limitation requirement buy stops external link collection **FIX
    allowed_domains = ["wiprodigital.com"]
    start_urls = ["http://wiprodigital.com/"]

    # Set rule base to allow following of links via Linkextractor class
    rules = (Rule(LinkExtractor(allow=()), callback='parse_items', follow=True),)

    def parse_items(self, response):

        # Don't assume web page structure, just grab all //divs as a started
        crawlpages = response.xpath('//div')
        items = []

        for pageinfo in crawlpages:
            item = ScraperItem()

            item['link'] = pageinfo.select("a/@href").extract()

            # Assume //img @src tag for images
            item['imageLink'] = pageinfo.select("a//img/@src").extract()

            # ignore blank entries
            if item['link'] or item['imageLink']:
                items.append(item)
        for item in items:
                yield item


