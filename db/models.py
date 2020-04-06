from sqlalchemy import Column, String, Integer, ForeignKey, DECIMAL, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class No(Base):
    __tablename__ = 'nos'

    id = Column(Integer, primary_key=True)
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)

    def __repr__(self):
        return f'< No(id="{self.id}", latitude="{self.latitude}", longitude="{self.longitude}") >'


class Aresta(Base):
    __tablename__ = 'arestas'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    no_1_id = Column(Integer, ForeignKey(No.id))
    no_2_id = Column(Integer, ForeignKey(No.id))

    def __repr__(self):
        return f'< Aresta(id="{self.id}", no_1="{self.no_1_id}", no_2="{self.no_2_id}") >'


class Estimativa(Base):
    __tablename__ = 'estimativas'

    id = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP)
    tempo = Column(DECIMAL)
    distancia = Column(DECIMAL)
    aresta_id = Column(Integer, ForeignKey(Aresta.id))

    def __repr__(self):
        return f'< Estimativa(id="{self.id}", timestamp="{self.timestamp}", tempo="{self.tempo}", distancia="{self.distancia}", aresta_id="{self.aresta_id}")>'
