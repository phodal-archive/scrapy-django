# -*- coding: utf-8 -*-
import json
import scrapy

from spider.items import GuokrItem


class GuokrSpider(scrapy.Spider):
    name = "guokr"
    allowed_domains = ["guokr.com"]
    start_urls = []
    for num in range(1, 2):
        start_urls.append("http://mooc.guokr.com/course/?page=" + str(num))

    def parse(self, response):
        for sel in response.css('.course_list li.course'):
            item = GuokrItem()
            item['title_en'] = sel.css('.course-title span')[0].xpath('text()').extract()[0]
            item['title_zh'] = sel.css('.course-title span')[1].xpath('text()').extract()
            if str(item['title_zh']) == '[]':
                item['title_zh'] = item['title_en']
            else:
                item['title_zh'] = item['title_zh'][0].replace('"', ",")

            item['link'] = sel.xpath('a/@href').extract()[0]
            item['count'] = sel.css(".course-info-num").xpath('text()').extract()[0]
            item['update_date'] = sel.css('.course-info-sp').xpath('text()').extract()
            yield item