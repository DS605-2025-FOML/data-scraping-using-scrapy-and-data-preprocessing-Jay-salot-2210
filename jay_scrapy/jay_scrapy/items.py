import scrapy

class JayScrapyItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()
    rating = scrapy.Field()
    product_page = scrapy.Field()  # URL of the book detail page
