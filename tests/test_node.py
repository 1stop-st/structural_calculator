from unittest import TestCase
from structural_calculator import Node
import numpy as np


class TestNode(TestCase):
    def test_initialized_node(self):
        n = Node()
        self.assertTrue(np.array_equal(n.position, (0., 0., 0.)))
        self.assertEqual(n.mass, 0)
        self.assertEqual(n.model, None)
        self.assertTrue(np.array_equal(n.displacement, (0., 0., 0., 0., 0., 0.)))
