import scrapy


class AmazonReviewSpider(scrapy.Spider):
    name = 'amazon_review'
    allowed_domains = ['']
    start_urls = ['http:///']

    def parse(self, response):
        pass
