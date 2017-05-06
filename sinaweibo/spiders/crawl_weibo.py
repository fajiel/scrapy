# -*- coding: utf-8 -*-
import scrapy
from sinaweibo.items import SinaweiboItem

class WeiboSpider(scrapy.Spider):
    name = "weibo"
    start_urls = (
        'http://weibo.com/tv/movie',
    )
    base_url = 'http://weibo.com'

    custom_settings = {
        'USER_AGENT':'spider',
    }

    def parse(self, response):
        items = response.css(".weibo_tv_frame").css(".li_list_1").xpath(".//a")
        for element in items:
            item = SinaweiboItem()
            item['url'] = self.base_url + element.css("a::attr(href)").extract_first()
            item['title'] = element.css("div[class='txt_cut']::text").extract_first().encode('UTF-8')
            item['image'] = element.css(".pic").xpath(".//img/@src").extract_first()
            item['duration'] = element.css(".categoryembd").css(".actplay")\
                                .css(".actcont-mins::text").extract_first()
            print item
            yield item