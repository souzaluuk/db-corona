from sqlalchemy import Column, String, Integer, Float, ForeignKey, Numeric, DateTime, Sequence
from sqlalchemy.ext.declarative import declarative_base
from decimal import Decimal

Base = declarative_base()


class Node(Base):
    __tablename__ = 'nodes'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    lat = Column(Numeric(10, 7), nullable=False)
    lon = Column(Numeric(10, 7), nullable=False)

    def __init__(self, lat, lon, name):
        self.id = None
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f'< Node(id="{self.id}", name="{self.name}", lat="{self.lat}", lon="{self.lon}") >'

    def __eq__(self, other):
        return isinstance(other, Node) and all([self.name == other.name, str(self.lat) == str(other.lat), str(self.lon) == str(other.lon)])


class Edge(Base):
    __tablename__ = 'edges'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    id_node_1 = Column(Integer, ForeignKey(Node.id), nullable=False)
    id_node_2 = Column(Integer, ForeignKey(Node.id), nullable=False)

    def __init__(self, name, id_node_1, id_node_2):
        self.id = None
        self.name = name
        self.id_node_1 = id_node_1
        self.id_node_2 = id_node_1

    def __repr__(self):
        return f'< Edge(id="{self.id}", name="{self.name}", id_node_1="{self.id_node_1}", id_node_2="{self.id_node_2}") >'

    def __eq__(self, other):
        return isinstance(other, Edge) and all([self.name == other.name, self.id_node_1 == other.id_node_1, self.id_node_2 == other.id_node_2])


class Distance(Base):
    __tablename__ = 'distances'

    id = Column(Integer, primary_key=True)
    stamp = Column(DateTime, nullable=False)
    time = Column(Float, nullable=False)
    dist = Column(Float, nullable=False)
    id_edge = Column(Integer, ForeignKey(Edge.id), nullable=False)

    def __init__(self, time, dist, id_edge):
        self.id = None
        self.id_edge = id_edge
        self.dist = dist
        self.time = time

    def __repr__(self):
        return f'< Distance(id="{self.id}", stamp="{self.stamp}", time="{self.time}", dist="{self.dist}", id_edge="{self.id_edge}") >'

    def __eq__(self, other):
        return isinstance(other, Distance) and all([self.id_edge == other.id_edge, self.dist == other.dist, self.time == self.time])
