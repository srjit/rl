
from components import Node, Edge

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


class StateGraph(object):
    
    def __init__(self, states=[], edges=[]):
        """
        
        Arguments:
        - `states`:
        - `edges`:
        """
        self._states = states
        self._edges = edges


    def add_state(self, state):
        """
    
        Arguments:
        - `self`:
        - `state`:
        """
        if(type(state) == Node):
            self._states.append(state)
         

    def add_edge(self, edge):
        """
    
        Arguments:
        - `self`:
        - `edge`:
        """
        if(type(edge) == Edge):
            self._edges.append(edge)
        

    def value(self, state):
        """
        
       Arguments:
        - `state`:
        """
        pass
   
