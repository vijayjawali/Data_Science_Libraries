# import scrapy
from scrapy.utils.response import open_in_browser

from ..items import QuotetutorialItem
#
#
# class QuoteSpider(scrapy.Spider):
#     name = "quotes"
#     page_number = 2
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/'
#     ]
#
#     def parse(self, response):
#         # title = response.css('title::text').extract_first()
#         # yield {'title': title}
#
#         items = QuotetutorialItem()
#
#         all_div_quotes = response.css('div.quote')
#         for quotes in all_div_quotes:
#
#             title = quotes.css('span.text::text').extract()
#             author = quotes.css('.author::text').extract()
#             tag = quotes.css('.tag::text').extract()
#
#             items['title'] = title
#             items['author'] = author
#             items['tag'] = tag
#
#             yield items
#
#         # next_page = response.css('li.next a::attr(href)').get()
#         # if next_page is not None:
#         #     yield response.follow(next_page, callback=self.parse)
#         # else:
#         #     print("No more pages")
#
#         next_page = 'http://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'
#
#         if QuoteSpider.page_number < 11:
#             QuoteSpider.page_number += 1
#             yield response.follow(next_page, callback=self.parse)
#         else:
#             print("No more pages")


import scrapy
from scrapy.http import FormRequest


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'abc@xyz.com',
            'password': 'abc123'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        items = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items