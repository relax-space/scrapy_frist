import scrapy
from scrapy.http.response import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.loader import ItemLoader
from scrapy.selector.unified import SelectorList
from scrapy_first.items import ScrapyFirstItem


class GiteeProjectSpider(scrapy.Spider):
    name = 'gitee-project'
    allowed_domains = ['gitee.com']
    domain = 'https://gitee.com'
    url_pre = f'{domain}/organizations/relax-space/projects?page='
    start_urls = [f'{url_pre}1']
    page_count = 3
    page_index = 1

    def parse(self, response: HtmlResponse):
        nodes: SelectorList = response.xpath('//*[@class="repository"]')
        for i in nodes:
            # [<Selector xpath='./@href' data='/relax-space/mybatis-first'>]
            loader = ItemLoader(ScrapyFirstItem(), selector=i)
            name = i.xpath('./text()').get()
            loader.add_value('name', name)
            if name == 'sample-data':
                link = i.xpath('./@href').get()
                yield Request(f'{self.domain}{link}',
                              callback=self.parse_info,
                              cb_kwargs={'loader': loader})
            else:
                yield loader.load_item()
        self.page_index += 1
        if self.page_index <= self.page_count:
            yield Request(f'{self.url_pre}{self.page_index}',
                          callback=self.parse)
        pass

    def parse_info(self, response: HtmlResponse, loader: ItemLoader):
        info = response.xpath(
            '//*[@class="file_content markdown-body"]/p/text()').get()
        loader.add_value('info', info)
        yield loader.load_item()
        pass
