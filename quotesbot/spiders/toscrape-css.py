# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'http://www.amazon.com/TRW-113415061C-Steering-Box-Beetle/dp/B00QXWZI7O',
    ]

    def parse(self, response):
        for product in response.css("div.ppd"):
            yield {
                'title': product.css("title_feature_div.span.text::text").extract_first(),
                #'author': quote.css("small.author::text").extract_first(),
                #'tags': quote.css("div.tags > a.tag::text").extract()
            }

        #next_page_url = response.css("li.next > a::attr(href)").extract_first()
        #if next_page_url is not None:
        #    yield scrapy.Request(response.urljoin(next_page_url))

