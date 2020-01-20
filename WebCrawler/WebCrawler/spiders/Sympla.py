# -*- coding: utf-8 -*-
import scrapy
from WebCrawler.items import EventItem
import sys
sys.path.append("/app-crawler")


from db.session_manager import session_scope
import WebCrawler.helpers.selectors as slc
from WebCrawler.helpers.helper import Helper

class SymplaSpider(scrapy.Spider):
    name = 'Sympla'
    allowed_domains = ['sympla.com.br']
    start_urls = ['http://sympla.com.br/eventos']
    count = 0

    def parse(self, response):
        for event in response.css(slc.EVENT_SELECTOR):
            link_event = event.css("a::attr(href)").extract_first()

            date_day = event.css(slc.INFO_DATE_DAY_EVENT).extract_first()
            date_month = event.css(slc.INFO_DATE_MONTH_EVENT).extract_first()
            date = Helper.build_date(date_day, date_month).extract_first(),
            event_info = dict(
                            date=date,
                            weekday=Helper.get_weekday(date),
                            time=event.css(slc.INFO_DATE_TIME_EVENT),
                            name=event.css(slc.INFO_NAME_EVENT),
                            local = Helper.get_local(event.css(slc.INFO_LOCAL_EVENT))
                         )

            yield response.follow(link_event, self.parse_event, cb_kwargs=event_info)

        more_event = response.css(slc.BUTTON_MORE_EVENT).extract_first()
        if more_event is not None:
            yield response.follow(more_event, self.parse)


    def parse_event(self, response, **event_info):
        # Aqui supostamente eu pegaria as informações de Ticket e a descrição
        #   da pagina de cada evento
        # Como tive problemas com captcha, vou mocar esses dados
        event_info["tipo_tickets"] = [
                    {"tipo_ticket": "Inteira", "valor_ticket": 40.00, "taxa_ticket": 4.00},
                    {"tipo_ticket": "Meia", "valor_ticket": 20.00, "taxa_ticket": 2.00}
                ]
        event_info["descricao"] = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing."

        event = EventItem(**event_info)
        yield event
