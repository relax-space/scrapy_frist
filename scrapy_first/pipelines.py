# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter


class ScrapyFirstWriterLinePipeline():

    def open_spider(self, spider):
        self.file = open('sample_first.jl', mode='w', encoding='utf8')
        pass

    def close_spider(self, spider):
        self.file.close()
        pass

    def process_item(self, item, spider):
        json.dump(ItemAdapter(item).asdict(), self.file, ensure_ascii=False)
        return item


class ScrapyFirstWriterJsonPipeline():

    def open_spider(self, spider):
        self.file = open('sample_first.json', mode='wb')
        self.exporter = JsonItemExporter(self.file, ensure_ascii=False)
        self.exporter.start_exporting()
        pass

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        pass

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class ScrapyFirstWriterCsvPipeline():

    def open_spider(self, spider):
        self.file = open('sample_first.csv',
                         mode='a',
                         newline='',
                         encoding='utf-8-sig')
        self.fieldnames = ['name', 'info']
        self.writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
        self.writer.writeheader()
        pass

    def close_spider(self, spider):

        self.file.close()
        pass

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item
