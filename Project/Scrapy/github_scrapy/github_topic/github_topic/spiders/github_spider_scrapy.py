# Import Libraries
import scrapy
#Import Items library from items.py where each title is saved
from ..items import GithubTopicItem
#import time library
import time

#Create spider
class topic(scrapy.Spider):
    name = "topic"
    start_urls = ["https://github.com/topics/"]

#Create parse class
    def parse(self, response):
#Instead of yielding for every variable we decide to create an items variable which will return all the title variable
        items = GithubTopicItem()
#to extract the required data from the website
        topic_title = response.xpath('//p[@class="f3 lh-condensed mb-0 mt-1 Link--primary"]/text()').extract()
        topic_desc = response.xpath('//p[@class="f5 color-text-secondary mb-0 mt-1"]/text()').extract()
        topic_link = response.xpath('//a[contains(@class,"d-flex no-underline")]/@href').extract()

#The dictionary to store the extracted data
        items['topic_title'] = topic_title
        items['topic_desc'] = topic_desc
        items['topic_link'] = topic_link

        yield items
#to calculate the runtime & performance of the code
        start = time.time()
        print("Running time: ", time.time() - start)

#To save in csv file please write below command in terminal
#scrapy crawl topic -o file.csv -t csv
