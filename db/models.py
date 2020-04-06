from sqlalchemy import Column, String, Integer, Float, ForeignKey, DECIMAL, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Node(Base):
    __tablename__ = 'nodes'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lat = Column(DECIMAL, nullable=False)
    lon = Column(DECIMAL, nullable=False)

    def __repr__(self):
        return f'< Node(id="{self.id}", name="{self.name}", lat="{self.lat}", lon="{self.lon}") >'


class Edge(Base):
    __tablename__ = 'edges'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    id_node_1 = Column(Integer, ForeignKey(Node.id), nullable=False)
    id_node_2 = Column(Integer, ForeignKey(Node.id), nullable=False)

    def __repr__(self):
        return f'< Edge(id="{self.id}", name="{self.name}", id_node_1="{self.id_node_1}", id_node_2="{self.id_node_2}") >'


class Distance(Base):
    __tablename__ = 'distances'

    id = Column(Integer, primary_key=True)
    stamp = Column(DateTime, nullable=False)
    time = Column(Float, nullable=False)
    dist = Column(Float, nullable=False)
    id_edge = Column(Integer, ForeignKey(Edge.id), nullable=False)

    def __repr__(self):
        return f'< Distance(id="{self.id}", stamp="{self.stamp}", time="{self.time}", dist="{self.dist}", id_edge="{self.id_edge}") >'
