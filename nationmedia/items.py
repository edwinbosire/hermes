# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class NationmediaItem(Item):
	title = Field()
	link = Field()
	category = Field()
	summary = Field()
	content = Field()
	author = Field()
	published = Field()
	image = Field()
	img_caption = Field()
	tag = Field()
	publisher = Field()