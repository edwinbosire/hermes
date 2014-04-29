from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from nationmedia.items import NationmediaItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

class MainParser():
    def __init__(self, response, tags):
        self.response = response
        self.tags = tags

    def scrapNationOnline(self):
        hxs = Selector(self.response)
        item = NationmediaItem()
        item ["tag"] = self.tags
        item ["link"] = self.response.url
        item ["published"] = ''.join(hxs.xpath('//div[@class=\"story-view\"]/header/h5/text()').extract())
        item ["title"]  = ''.join(hxs.xpath('//div[@class=\"story-view\"]/header/h1/text()').extract()) #this worked by taking the page title, contains tags we dont need/want ''.join(hxs.css('title::text').extract())
        item ["summary"] = ''.join(hxs.xpath('//div/ul/li/text()').extract())
        item ["content"] = '\n'.join(hxs.xpath('//article/section/div/p/text()').extract())
        item ["image"] = 'http://www.nation.co.ke'.join(hxs.xpath('//img[@class=\"photo_article\"]/@src').extract())
        item ["img_caption"] = ''.join(hxs.xpath('//img[@class=\"photo_article\"]/@alt').extract())

        #retrieve the author. There are numerous formatting issue with this tag

        author = hxs.xpath('//section[@class=\"author\"]/strong/text()').extract()
        if not author:
            author = hxs.xpath('//section[@class=\"author\"]/text()').extract()
        item ["author"] = ''.join(author)

        return item

class PoliticsSpider(CrawlSpider):
    """Scrapes Polics News"""
    name = "politics"
    allowed_domains = ["nation.co.ke"]
    start_urls = ["http://www.nation.co.ke/news/politics/-/1064/1064/-/3hxffhz/-/index.html"]
    rules = (
        Rule(SgmlLinkExtractor(allow=('news\/politics\/',), deny=('\/view\/asFeed\/', '\/-\/1064\/1064\/-\/3hxffhz\/-\/index.html')), callback='parse_page', follow=True),
    )
    def parse_page(self, response):
        mainParser = MainParser(response, ["News", "Politics"])
        item = mainParser.scrapNationOnline()
        return item


class BusinessSpider(CrawlSpider):
    """Scrapes Business News"""
    name = "business"
    allowed_domains = ["nation.co.ke"]
    start_urls = ["http://www.nation.co.ke/business/-/996/996/-/xt3q8cz/-/index.html"]
    rules = (
        Rule(SgmlLinkExtractor(allow=('business\/',), deny=('\/view\/asFeed\/')), callback='parse_page', follow=True),
    )
    def parse_page(self, response):
        mainParser = MainParser(response, ["Business", "Corporates", "Enterprise", "Markets"])
        item = mainParser.scrapNationOnline()
        return item

class TechnologySpider(CrawlSpider):
    """Scrapes Technology News"""
    name = "technology"
    allowed_domains = ["nation.co.ke"]
    start_urls = ["http://www.nation.co.ke/business/Tech/-/1017288/1017288/-/g8v3dnz/-/index.html"]
    rules = (
        Rule(SgmlLinkExtractor(allow=('business\/Tech\/',), deny=('\/view\/asFeed\/')), callback='parse_page', follow=True),
    )
    def parse_page(self, response):
        sel = Selector(response)
        mainParser = MainParser(response, ["Technology"])
        item = mainParser.scrapNationOnline()
        return item

class SportsSpider(CrawlSpider):
    """Scrapes Sports News"""
    name = "sports"
    allowed_domains = ["nation.co.ke"]
    start_urls = ["http://www.nation.co.ke/sports/-/1090/1090/-/4uk06mz/-/index.html"]
    rules = (
        Rule(SgmlLinkExtractor(allow=('sports\/',), deny=('\/view\/asFeed\/')), callback='parse_page', follow=True),
    )
    def parse_page(self, response):
        mainParser = MainParser(response, ["Sports"])
        item = mainParser.scrapNationOnline()
        return item
