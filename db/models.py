import sqlalchemy as db
from . import Base

class Evento(Base):
    __tablename__ = "eventos"
    id = db.Column(db.Integer(), primary_key=True, nullable = False)
    nome_evento = db.Column(db.String(length=50))
    nome_local = db.Column(db.String(length=50))
    cidade_local = db.Column(db.String(length=30))
    descricao = db.Column(db.Text(4294000000))
    data_evento = db.Column(db.Date())
    hora_evento = db.Column(db.Time())
    dia_semana = db.Column(db.String())
    data_registro = db.Column(db.DateTime(), default=db.func.now())
    tipo_tickets = db.orm.relationship("TipoTicket", backref="eventos")

class TipoTicket(Base):
    __tablename__ = "tipo_tickets"
    id = db.Column(db.Integer(), primary_key=True, nullable = False)
    id_eventos = db.Column(db.Integer(), db.ForeignKey('eventos.id'), nullable = False)
    tipo_ticket = db.Column(db.String(20))
    valor_ticket = db.Column(db.Numeric(precision=6, scale=2))
    taxa_ticket = db.Column(db.Numeric(precision=6, scale=2))
    evento = db.orm.relationship("Evento", backref="tipo_tickets")