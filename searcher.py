#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Brandon Bouley
# email: bbouley@bu.edu


import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    
    
    def __init__(self, depth_limit):
        """a constructor for a Searcher object, one that tracks 
        the number of states tested"""
        self.states=[]
        self.num_tested=0
        self.depth_limit=depth_limit
        
        

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
    
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def add_state(self, new_state):
        """appends State new_state to object Searcher's state
        list"""
        self.states+=[new_state]
        
    def should_add(self,state):
        """takes a State object called state and returns True
        if the called Searcher should add state to its list 
        of untested states, and False otherwise"""
        if state.creates_cycle():
            return False
        elif self.depth_limit!=-1 and state.num_moves>self.depth_limit:
            return False
        else:
            return True
        
    def add_states(self, new_states):
        """uses helper function add state to add applicable states
        into the available state list"""
        for i in new_states:
            if self.should_add(i):
                self.add_state(i)
                
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """creates new generations of sucessors until a board
        in the goal state is found"""
        self.add_state(init_state)
        while self.states!=[]:
            s = self.next_state()
            self.num_tested+=1
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
        return None
    
    
        
# BF Searcher:  

class BFSearcher(Searcher):
    """a searcher that finds the solution in the minimum
    depth"""
    
    def next_state(self):
        """only new method of BFS, changes next_state so it removes
        the newest state in the list"""
        
        s=self.states[0]
        self.states.remove(s)
        return s
    
# DF Searcher:

class DFSearcher(Searcher):
    """a searcher that reaches the maximum depth it can before 
    returning a solution"""
    
    def next_state(self):
        """ only new method of DFS, changes next_state so it
        only removes the oldest state in the list"""
        
        s=self.states[-1]
        self.states.remove(s)
        return s
    

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def h1(state):
    """a heuristic function that returns the number of misplaced
    tiles"""
    return state.board.num_misplaced()

def h2(state):
    """ a heuristic function that returns the combined number
    of tiles in the wrong row and tiles in the wrong column"""
    return state.board.misplaced_rowcol()

# Greedy Searcher:
class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    
    def __init__(self,heuristic):
        """constructor for Greedy, only new value is heuristic
        which defines the priority of the states it searches"""
        
        super().__init__(-1)
        
        self.heuristic=heuristic
        


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
       
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        """modification of add_state to include priority"""
        self.states+=[[self.priority(state) , state]]
        
    def next_state(self):
        """modification of next_state that removes the state with
        the highest priority"""
        s = max(self.states)
        s1 = s[-1]
        self.states.remove(s)
        return s1
        

# A* Searcher:

class AStarSearcher(GreedySearcher):
    """informed search algorithm that assigns a priority to
    each state based on a heuristic function, takes into account
    moves already extended to get to that state"""
    
    def __init__(self,heuristic):
        
        """constructor A*, which inherits from Greedy
        and doesnt do much else"""
        
        super().__init__(heuristic)
    
    def priority(self, state):
        """new priority system for A*, one that accounts for
        moves extended to reach given position."""
        return -1 * (self.heuristic(state) + state.num_moves)
    
    