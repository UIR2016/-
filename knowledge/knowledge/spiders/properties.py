# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import PropertyItem

class PropertiesSpider(scrapy.Spider):
    name = 'properties'
    allowed_domains = ['www.thefamouspeople.com']
    start_urls = ['http://www.thefamouspeople.com/political-leaders.php']

    def parse(self, response):
	    #extract leader's url
	    le = LinkExtractor(restrict_css='a.tileLink')
	    Link = le.extract_links(response)
	    for link in  Link:
		    yield scrapy.Request(link.url,callback=self.parse_properties)
	    #next page
	    url = response.css('li.nextpage').xpath('.//a[contains(string(.),"Next")]/@href').extract_first()
	    if url:
		    url = response.urljoin(url)
		    yield scrapy.Request(url,callback = self.parse)
    #get properties
    def parse_properties(self,response):
	    # locat div
	    el = response.css('div.fps-desc.fpf-block')
	    #sring*2 by  : 
	    Pel = el.css('p.quickfactsdata').xpath('string(.)')
	    for pel in Pel:
		    #array
		    arr = pel.extract().split(':')
		    item = PropertyItem()
		    #locat h1 
		    item['entity'] = response.css('h1').xpath('string(.)').extract_first()
		    #verify
		    if len(arr)==2:
			    item['type1'] = arr[0]
			    item['thing'] = arr[1]
			    yield item
