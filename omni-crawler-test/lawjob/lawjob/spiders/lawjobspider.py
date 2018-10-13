from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from lawjob.items import LawjobItem
from scrapy.http.request import Request
from urllib.parse import urljoin





class Lawjobspider(Spider):

    name = "lawjobspider"

    start_urls = ['https://www.simplylawjobs.com/jobs']


    def parse(self, response):
        joblist = response.xpath('//li[@class="job"]')
        links = joblist.xpath('//li[@class="job"]/div/div[@class="buttons"]/a[@class="button radius view_job_btn"]/@href').extract()
        for link in links:
            yield Request(urljoin('https://www.simplylawjobs.com:', link), callback=self.detail_page)



    def detail_page(self, response):

        Job = ItemLoader(item=LawjobItem(), selector=response)

        Job.add_xpath('title', '//div[@class="columns small-12 medium-4 large-4 details"]/h1/text()')
        yield Job.load_item()


