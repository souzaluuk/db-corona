from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Node, Edge, Distance, Base

import unittest


class TestNode(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///dev.sqlite')
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_insert_nodes(self):
        nodes = [
            Node(1, -1.4513525, -48.4689927, 'Av. Alm. Barroso x São Brás'),
            Node(2, -1.4053284, -48.4330374, 'Av. Alm. Barroso x Entroncamento'),
            Node(3, -1.4049556, -48.4326765,
                 'Av. Alm. Barroso x Entroncamento'),
            Node(id=4, lat=-1.4510252, lon=-48.4690023,
                 name='Av. Alm. Barroso x São Brás')
        ]
        session = Session(self.engine)
        session.add_all(nodes)
        session.commit()

        query = Session(self.engine).query(Node)

        self.assertEqual(query.count(), len(nodes))

        def node_equal(current, exp):
            return all(
                [
                    current.id == exp.id,
                    current.name == exp.name,
                    current.lat == exp.lat,
                    current.lon == exp.lon
                ]
            )

        for index in range(len(nodes)):
            self.assertTrue(node_equal(nodes[index], query.get(index+1)))

        node10 = Node(id=10, lat=-1.4538671, lon=-48.4925673,
                      name='Av. Assis de Vasconcelos x Av. Nazaré')
        session.add(node10)
        session.commit()

        self.assertTrue(node_equal(node10, Session(
            self.engine).query(Node).get(10)))

        session.add(Node(id=None, lat=-1.4538671, lon=-48.4925673,
                         name='Av. Assis de Vasconcelos x Av. Nazaré'))
        session.commit()
        self.assertIsNotNone(Session(self.engine).query(Node).get(11))

        for index in range(5, 10):
            self.assertIsNone(Session(
                self.engine).query(Node).get(index))


if __name__ == "__main__":
    unittest.main()
