
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

    def add_states(self, states):
        """
    
        Arguments:
        - `self`:
        - `states`:
        """
        list(map(self.add_state, states))
         

    def add_edge(self, edge):
        """
    
        Arguments:
        - `self`:
        - `edge`:
        """
        if(type(edge) == Edge):
            self._edges.append(edge)
            

    def add_edges(self, edges):
        """
    
        Arguments:
        - `self`:
        - `edges`:
        """
        list(map(self.add_edge, edges))


       
    def get_all_connected_edges(self, state):
        """
        
        Arguments:
        - `states`:
        """
        
        return [x for x in self._edges if x._source == state]

        
        


        

    def value_function(self, state):
        """
       Arguments:
        - `state`:
        """
        connected_edges = self.get_all_connected_edges(state)
        pass
   
