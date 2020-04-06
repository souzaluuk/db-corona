from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Node, Edge, Distance, Base

import unittest


class TestNode(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = Session(self.engine)
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_insert_nodes(self):
        node1 = Node(lat=-1.447221, lon=-48.462076,
                     name='Tv. Antônio Baena x Av. João Paulo II')
        node2 = Node(lat=-1.445499, lon=-48.464657,
                     name='Tv. Antônio Baena x Av. Almt. Barroso')

        nodes = [node1, node2]
        self.session.add_all(nodes)

        query = Session(self.engine).query(Node)

        self.assertEqual(query.count(), 0)
        self.session.commit()
        self.assertEqual(query.count(), len(nodes))


if __name__ == "__main__":
    unittest.main()
