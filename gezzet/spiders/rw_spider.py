import scrapy

from gezzet.items import RwItem
class RwSpider(scrapy.Spider):
    name = "rw_spider"
    allowed_domains = [ "http://www.primature.gov.rw/" ]
    start_urls = ["http://www.primature.gov.rw/index.php?id=54"]

    def parse(self, response):
            for href in response.css(".tx-filelist-pi1-filename a"):
                url = response.urljoin(href.extract())
                yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse(self, response):
        for sel in response.xpath('//*[(@id = "c36")]//a'):

            item = RwItem()
            item['filename'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item















# //*[contains(concat( " ", @class, " " ), concat( " ", "tx-filelist-pi1-filename", " " ))]//a

# //*[(@id = "c36")]//a
