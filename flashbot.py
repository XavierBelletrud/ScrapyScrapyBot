import scrapy
from scrapy import Request

     
     
class MyScrapyBot(scrapy.Spider):
    name = 'MonsterBot'
    allowed_domains = ['http://rss.jobsearch.monster.com/rssquery.ashx?q=big']
    start_urls = ['http://rss.jobsearch.monster.com/rssquery.ashx?q=big']
     
      
    def parse(self, response):
        for post in response.xpath('//channel/item'):
            yield {
                'title' : post.xpath('title//text()').extract_first(),
                'description' : post.xpath('description//text()').extract_first(),
                'link': post.xpath('link//text()').extract_first(),
                'guid' : post.xpath('guid//text()').extract_first(),
                'pubDate' : post.xpath('pubDate//text()').extract_first()}