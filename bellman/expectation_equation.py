from components import State, Action
from states import StateGraph

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


def get_nodes():
    
    return [State(1, "S1", -2.3), State(2, "S2", -1.3), State(3, "S3", 0),
            State(4, "S4", 2.7), State(5, "S5", 0), State(5, "S6", 7.4)]


def get_states_and_actions():
    
    nodes = get_nodes()
    
    return [nodes, [Action("Facebook", nodes[0], nodes[0], 0.5, -1),
            Action("Quit", nodes[0], nodes[1], 0.5, 0),

            Action("Facebook", nodes[1], nodes[0], 0.5, -1),
            Action("Study", nodes[1], nodes[3], 0.5, -2),

            Action("Sleep", nodes[3], nodes[4], 0.5, 0),
            Action("Study", nodes[3], nodes[5], 0.5, -2),

            Action("A1", nodes[4], nodes[1], 0.2, 0),
            Action("A2", nodes[4], nodes[3], 0.4, 0),
            Action("A3", nodes[4], nodes[5], 0.4, 0),

            Action("Study", nodes[5], nodes[2], 0.5, 10),
            Action("Pub", nodes[5], nodes[4], 0.5, 1)]]
    

states_and_actions = get_states_and_actions()
sg = StateGraph(states_and_actions[0], states_and_actions[1])
print(sg.bellman_expectation_for_state(3))
