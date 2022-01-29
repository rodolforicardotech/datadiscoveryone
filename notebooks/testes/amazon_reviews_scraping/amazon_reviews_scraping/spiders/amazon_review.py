import scrapy
import sys

class AmazonReviewsSpider(scrapy.Spider):

    # Spider name
    name = 'amazon_reviews'

    # Domain names to scrape
    allowed_domains = ['amazon.com.br']
    # Base URL for the MacBook air reviews
    arq = open('testes/dominio.txt','r')
    
    myBaseUrl = list(arq)[0]#"https://www.amazon.com.br/Multilaser-TC212-Teclado-Entrada-Multimidia/product-reviews/B075KGTFKM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    arq.close()
    start_urls=[]
    #start_urls.append(myBaseUrl)
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(2,100):
        start_urls.append(myBaseUrl+'&pageNumber='+str(i))
    def parse(self, response):

            data = response.css('#cm_cr-review_list')

            # Collecting product star ratings
            star_rating = data.css('.review-rating')

            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0

            # Combining the results
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
                count=count+1