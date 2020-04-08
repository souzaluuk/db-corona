from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Node, Edge, Distance, Base

import unittest


class TestNode(unittest.TestCase):
    engine = create_engine(
        'postgresql://corona_tests:corona_tests@0.0.0.0:54321/corona_tests', echo=True)
    Session = sessionmaker(bind=engine)

    def setUp(self):
        self.session = self.Session()
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_insert_nodes(self):
        nodes_args = [
            (1, -1.4513525, -48.4689927, 'Av. Alm. Barroso x São Brás'),
            (2, -1.4053284, -48.4330374, 'Av. Alm. Barroso x Entroncamento'),
            (3, -1.4049556, -48.4326765, 'Av. Alm. Barroso x Entroncamento'),
            (4, -1.4510252, -48.4690023, 'Av. Alm. Barroso x São Brás')
        ]

        for (id_, lat, lon, name) in nodes_args:
            self.session.add(Node(lat, lon, name))
        self.session.commit()

        self.assertEqual(self.session.query(Node).count(), len(nodes_args))

        for (id_, lat, lon, name) in nodes_args:
            self.assertEqual(self.session.query(
                Node).get(id_), Node(lat, lon, name))

        self.session.add(Node(lat=-1.4538671, lon=-48.4925673,
                              name='Av. Assis de Vasconcelos x Av. Nazaré'))
        self.session.add(Node(-1.4606754, -48.4826942,
                              'Av. Assis de Vasconcelos x Av. Mal. Hermes'))
        self.session.commit()

        self.assertEqual(self.session.query(Node).count(), len(nodes_args)+2)
        self.assertIsNotNone(self.session.query(Node).get(5))
        self.assertIsNotNone(self.session.query(Node).get(6))

        for index in range(7, 10):
            self.assertIsNone(self.session.query(Node).get(index))
        self.session.commit()


if __name__ == "__main__":
    unittest.main()
