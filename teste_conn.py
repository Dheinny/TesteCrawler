from db.session_manager import session_scope
from db.models import Evento, TipoTicket

with session_scope() as session:
    tipo_ticket = TipoTicket(
        id_eventos = 2,
        tipo_ticket = "Gratis",
        valor_ticket = 5.00,
        taxa_ticket = 0.5
    )

    evento = Evento(
        nome_evento="Carnaval",
        nome_local="Bloco de Rua",
        cidade_local="Campinas, sp",
        data_evento="2010-01-25",
        hora_evento="19:30",
        dia_semana="Sab",
        tipo_tickets = [tipo_ticket]
    )

    #session.add(evento)
    a = session.query(TipoTicket).all()


########## TODO LIST ###############
# - Dar um jeito de pegar os tipos de ingresso
#       Como o captcha está atrapalhando, provavelmente terei q mocar..
# - Fazer o objeto de retorno e criar um PIPELINE pra salvar no banco.
# - Popular banco com alguns eventos, na mão (mockado)
# - Criar os SQLs pedidos na tarefa
# - DOCUMENTAR
# - Criar um git e dar autorização