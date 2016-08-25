from elasticsearch_dsl import DocType


class Crunchyroll_article( DocType ):
    link  = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    source = scrapy.Field()
    tags = scrapy.Field()
    videos = scrapy.Field()
