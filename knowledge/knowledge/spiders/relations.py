# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import RelationItem
class RelationsSpider(scrapy.Spider):
    name = 'relations'
    allowed_domains = ['www.thefamouspeople.com']
    start_urls = ['https://www.thefamouspeople.com/political-leaders.php']

    def parse(self, response):
	    #extract leader's url
	    le = LinkExtractor(restrict_css='a.tileLink')
	    Link = le.extract_links(response)
	    #put link to next parse
	    for link in Link:
		    yield scrapy.Request(link.url,callback = self.parse_relation)
	    #next page
	    url = response.css('li.nextpage').xpath('.//a[contains(string(.),"Next")]/@href').extract_first()

	    if url:
		    url = response.urljoin(url)
		    yield scrapy.Request(url,callback = self.parse)
    
    #parse relation
    def parse_relation(self,response):
	    
	    
	    
	    
	    #get relation&entity2
	    le=response.css('div.family')
	    
	    Rle = le.css('p.quickfactsdata').xpath('string(.)')
	    for rle in Rle:
		    str2 = rle.extract()




	    # get by array
	    

		    rela_enti2 = str2.split(':')
		    item = RelationItem()
		    
		    item['entity'] = response.css('h1').xpath('string(.)').extract_first()

		    item['typee'] = rela_enti2[0]
		    item['thing'] = rela_enti2[1]
		    yield item
					


