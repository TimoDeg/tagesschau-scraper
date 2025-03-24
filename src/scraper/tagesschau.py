import scrapy

class Tagesschau(scrapy.Spider):
    name = "tagesschau"
    start_urls = ["https://www.tagesschau.de/infoservices/alle-meldungen-100~rss2.xml"]

    def parse(self, response):
        i = 0
        for item in response.xpath("//channel/item"):
            yield{
                "title": item.xpath("title/text()").get(),
                "link": item.xpath("link/text()").get(),
                "description": item.xpath("description/text()").get(),
                "pub_date": item.xpath("pubDate/text()").get() 
            }
            