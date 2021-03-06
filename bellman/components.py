
__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


class State(object):
    
    def __init__(self, _id, name, reward):
        self._id = _id
        self._name = name
        self._reward = reward

    
    def __str__(self):
        return "{" + \
              " Id: "+ str(self._id) + "," + \
              " Name: "+ self._name + \
              " }\n"



class Action(object):
    
    def __init__(self, action, source, destination, tp, reward=0):
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
        self._reward = reward



    def __str__(self):
        """
        
    Arguments:
        - `self`:
        """
        return("{" + \
              " Action : "+ self._action + "," \
              " Source "+ self._source + \
              " }\n")



