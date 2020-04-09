from db.settings import Session, engine
from db.models import Node, Edge, Base
from sqlalchemy.orm import aliased
import csv

Base.metadata.create_all(engine)
session = Session()

# Insert Nodes
with open('db/csv/map-brendo.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        lon, lat, name = row
        session.add(Node(lat, lon, name))
session.commit()
# Print all inserted nodes
all_nodes = session.query(Node).all()
for node in all_nodes:
    print(node)

# Insert Edges
pairs_nodes = zip(all_nodes[::2], all_nodes[1::2])
for node_1, node_2 in pairs_nodes:
    name_edge = node_1.name.split('x')[0]
    name_edge += '-'+node_1.name.split('-')[-1] if '-' in node_1.name else ''
    session.add(Edge(name_edge, node_1.id, node_2.id))
session.commit()
# Print all Edges
n_1 = aliased(Node)
n_2 = aliased(Node)
for edge in session.query(Edge.name, n_1.name, n_2.name).join(n_1, n_1.id == Edge.id_node_1).join(n_2, n_2.id == Edge.id_node_2).all():
    print(edge)
session.commit()
Base.metadata.drop_all(engine)