import numpy as np
from components import Node, Edge

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


class StateGraph(object):
    
    def __init__(self, states=[], edges=[], discounting_factor=0.5):
        """
        
        Arguments:
        - `states`:
        - `edges`:
        """
        self._states = states
        self._edges = edges
        self._discounting_factor = discounting_factor


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

        
    def get_all_connected_states(self, edges):
        """
    
    Arguments:
    - `self`:
    - `edges`:
    """
        return [x._destination for x in edges]


    def _get_tps_of_state(self, state):
        _tps = [0.0 for x in self._states]

        connected_edges = self.get_all_connected_edges(state)        
        probs = [edge._tp for edge in connected_edges]

        states_connected_at_edges = self.get_all_connected_states(connected_edges)
        state_ids = [x._id for x in states_connected_at_edges]

        prob_counter = 0
        for i in state_ids:
            _tps[i] = probs[prob_counter]
            prob_counter+=1
        return _tps


    def transition_probability_matrix(self):
        return [self._get_tps_of_state(state) for state in self._states]


    ##calculate value function of all states 
    def value_function_of_all_states(self):
        """
        """
        tps = self.transition_probability_matrix()
        transition_probability_matrix = np.array(tps)
        num_states = len(self._states)
        tmp = np.linalg.inv(np.identity(num_states) - self._discounting_factor * transition_probability_matrix)
        rewards = [x._reward for x in self._states]
        return rewards - tmp
        



    

    
