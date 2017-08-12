


__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"



    ## Error in the formula -  second multiplier must be value
    ## function of the subsequent states and not the reward function
    def value_function(self, state):
        """
       Arguments:
        - `state`:
        """
        connected_edges = self.get_all_connected_edges(state)
        transition_probabilities = [x._tp for x in connected_edges]
        states_connected_at_edges = self.get_all_connected_states(connected_edges)
        rewards_at_connected_states = [x._reward for x in states_connected_at_edges]
        return sum([a*b for a,b in zip(transition_probabilities, rewards_at_connected_states)])
