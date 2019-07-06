import numpy as np


class Node:
    """
    Representing a Node object.
    Nodes connect members.
    """
    def __init__(self):
        self.position = np.zeros(3)
        self.mass = 0.
        self.displacement = np.zeros(6)
        self.model = None
