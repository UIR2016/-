# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KnowledgeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    entity = scrapy.Field()
    type1 = scrapy.Field()
    thing = scrapy.Field()
class PropertyItem(scrapy.Item):

    entity = scrapy.Field()
    type1 = scrapy.Field()
    thing = scrapy.Field()
class RelationItem(scrapy.Item):

    entity = scrapy.Field()
    thing = scrapy.Field()
    typee = scrapy.Field()
