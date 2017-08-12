

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


class Node(object):
    
    def __init__(self, _id, name, reward):
        """
        
        Arguments:
        - `name`: Name of the state
        - `reward`: Reward for the state
        """
        self._id = _id
        self._name = name
        self._reward = reward
        


class Edge(object):
    
    def __init__(self, action, source, destination, tp):
        """
        
        Arguments:
        - `source`: The source node
        - `action`: The name of the action
        - `destination`: The destination
        - `tp`: Transition probability
        """
        self._action = action
        self._source = source
        self._destination = destination
        self._tp = tp
