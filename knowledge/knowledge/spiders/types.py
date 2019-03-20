# -*- coding: utf-8 -*-
import scrapy

from ..items import KnowledgeItem #用哪个item就调用哪了，以-o输出的话定义items的结构就是输出的样子

class TypesSpider(scrapy.Spider):
    name = 'types'
    allowed_domains = ['www.thefamouspeople.com']
    #起始页
    start_urls = ['https://www.thefamouspeople.com/political-leaders.php']

    def parse(self, response):
	    #爬取entity
	    for eel in response.css('a.tileLink'):
		    item = KnowledgeItem()
		    item['entity'] = eel.css('img::attr(title)').extract_first()
		    item['type1'] = '<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>'
		    item['thing'] = 'political-leaders'
		    yield item
	    #解决翻页那个难点
	    #拼接next页的url，css，xpath语法看教程吧
	    #提取含Next的url，有的话回滚到开始
	    url=response.css('li.nextpage').xpath('.//a[contains(string(.),"Next")]/@href').extract_first()
	    if url:
		    url = response.urljoin(url)
		    yield scrapy.Request(url,callback = self.parse)
   
