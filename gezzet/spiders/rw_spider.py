import scrapy

from gezzet.items import RwItem
class RwSpider(scrapy.Spider):
    name = "rw_spider"
    allowed_domains = [ "http://www.primature.gov.rw/" ]
    start_urls = ["http://www.primature.gov.rw/index.php?id=8",
                  "http://www.primature.gov.rw/index.php?id=8&tx-filelist-pi1-36[path]=Official%20Gazettes&cHash=cc3451c98736783ac5d3751637a3a179"
                ]

    def parse(self, response):
        for sel in response.xpath('//*[(@id = "c36")]//a'):

            item = RwItem()
            item['filename'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
