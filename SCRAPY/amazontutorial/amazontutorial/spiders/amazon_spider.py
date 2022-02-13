import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1644741545&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0'
    ]

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css('.a-size-medium').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.s-link-style').css('::text').extract()
        product_price = response.css('.s-price-instructions-style .a-price-whole').css('::text').extract()
        prroduct_imagelink = response.css('.s-image').css('::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = prroduct_imagelink

        yield items

        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=' + str(AmazonSpiderSpider.page_number) + '&qid=1644741554'

        if AmazonSpiderSpider.page_number <= 100:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
