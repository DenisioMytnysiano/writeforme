import scrapy


class Poem(scrapy.Item):
    name: str = scrapy.Field()
    written_by: str = scrapy.Field()
    poem: str = scrapy.Field()
