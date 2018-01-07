from scrapy import Spider
from scrapy import Selector


class PictureSpider(Spider):
    name = "PictureSpider"
    allow_domains = ["www.ikkwt.com"]
    start_urls = [
        "http://www.ikkwt.com/pingtai/",
    ]

    def parse(self, response):
        selector = Selector(response)
        sites = selector.xpath("//li[@class='platform-list']")
        for site in sites:
            print("------------------------------------------------------------")
            platform_name = site.xpath("div/div/h2/a/text()").extract()[0]
            platform_type = site.xpath("//span[@class='column']/span/text()").extract()[0]
            platform_least = site.xpath("//span[@class='column']/span/text()").extract()[1]
            platform_charge = site.xpath("//span[@class='column']/span/text()").extract()[2]
            category = site.xpath("div/div[@class='platform-foot']/p/text()").extract()[0]

            print("Platform : " + platform_name)
            print("Remark : " + platform_type + ", " + platform_least + ", " + platform_charge)
            print("Category : " + category)
