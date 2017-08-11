from components import Node, Edge
from states import StateGraph

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


def get_nodes():
    
    return [Node(0, "Class1", -2), Node(1, "Facebook", -1), Node(2, "Class2", -2),
            Node(3, "Class3", -2), Node(4, "Sleep", 0),
            Node(5, "Pub", -1)]


def get_edges(nodes):
    return [Edge("Facebook", nodes[0], nodes[1], 0.5),
            Edge("Study", nodes[0], nodes[2], 0.5),

            Edge("Facebook", nodes[1], nodes[1], 0.9),
            Edge("Quit", nodes[1], nodes[0], 0.1),

            Edge("Study", nodes[2], nodes[3], 0.8),
            Edge("Study", nodes[2], nodes[5], 0.2),

            Edge("Study", nodes[3], nodes[4], 0.8),
            Edge("Pub", nodes[3], nodes[6], 0.0),

            Edge("", nodes[5], nodes[0], 0.2),
            Edge("", nodes[5], nodes[2], 0.4),
            Edge("", nodes[5], nodes[3], 0.4)]


sg = StateGraph()
sg.add_states(get_nodes())
sg.add_edges(get_edges(sg._states))
