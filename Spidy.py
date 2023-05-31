from asyncio.windows_events import NULL
import scrapy
import re
from colorama import Fore, Style
import keyboard
import networkx as nx
import matplotlib.pyplot as plt
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider



key_pressed = False


class MySpider(scrapy.Spider):
    name = "Spidy"
    start_urls = ["http://sylib.org/"]
    url_map = {}
    graph = NULL

    def key_listener(self, event):
        if event.name == 'esc':
            global key_pressed
            key_pressed = True


    def __init__(self):
        print('Press Esc To Stop And Show The Graph')
        self.graph = nx.DiGraph()
        keyboard.on_press(self.key_listener)


    def parse(self, response):

        # Extract specific elements from the webpage
        # Example: Extract all the links on the webpage

        #using CSS selector
        #links = response.css("a::attr(href)").getall()
        
        if key_pressed == False:
            links = response.xpath("//a/@href").getall()

            self.url_map[response.url] = []

            for link in links:
                if (self.is_valid_link(link) and link != response.url):
                    self.url_map[response.url].append(link)
                    yield scrapy.Request(url=response.urljoin(link), callback=self.parse)

        
        else:
            return

    def is_valid_link(self, link):
            # Define a regular expression pattern for link validation
            pattern = r'^http'
            return re.match(pattern, link) is not None

    def show_chart(self):

        for key in self.url_map:
            self.graph.add_node(key)

        for key, value in self.url_map.items():
            for item in value:
                self.graph.add_edge(key, item)

        pos = nx.spring_layout(self.graph, k=1.2)
        plt.figure(figsize=(10, 6))
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', edge_color='blue', node_size=2000, font_size=10)
        plt.title("URL Relational Chart")
        plt.show()


    def spider_closed(self, spider, reason):
        # Code to execute after the spider finishes
        self.show_chart()

# Run the spider
if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess({'LOG_ENABLED': False})
    spider = MySpider()
    crawler = process.create_crawler(MySpider)
    crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
    process.crawl(crawler)
    process.start()