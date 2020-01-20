# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from db.session_manager import session_scope
from db.models import Evento, TipoTicket
from WebCrawler.helpers.models_builder import ModelBuilder

class WebcrawlerPipeline(object):
    def process_item(self, item, spider):
        with session_scope() as session:
            evento = ModelBuilder.build_evento_model(item)
            session.add(evento)

        return item


