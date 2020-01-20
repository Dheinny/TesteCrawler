from WebCrawler.WebCrawler.items import EventItem
from db.models import Evento, TipoTicket

class ModelBuilder():

    @staticmethod
    def build_evento_model(eventItem):
        evento = Evento(
            nome_evento=eventItem.name,
            nome_local=eventItem.local["nome_local"],
            cidade_local=eventItem.local["cidade_local"],
            data_evento=eventItem.date,
            hora_evento=eventItem.time,
            dia_semana=eventItem.weekday,
            tipo_tickets=BuilderModel.build_tipo_ticket_model(eventItem.tipo_tickets)
        )
        return evento

    @staticmethod
    def build_tipo_ticket_model(tipo_tickets):
        tipo_tickets_list = []
        for tipo_ticket in tipo_tickets:
            tipo_ticket = TipoTicket(
                tipo_ticket=tipo_tickets["tipo_ticket"],
                valor_ticket=tipo_tickets["valor_ticket"],
                taxa_ticket=tipo_tickets["taxa_ticket"]
            )
            tipo_tickets.append(tipo_ticket)
        return tipo_tickets_list