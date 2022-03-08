#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: brandon bouley
# email: bbouley@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
    
    def __init__(self,board,predecessor,move):
        """a constructor for a State object, one that specifies
        the state of the input board"""
        self.board=board
        self.predecessor=predecessor
        self.move=move
        if predecessor==None:
            self.num_moves=0
        else:
            self.num_moves=predecessor.num_moves+1
            

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
    
    def is_goal(self):
        """checks if the current board state is a win state"""
        
        return self.board.tiles==GOAL_TILES
            
    def generate_successors(self):
        """generates a list of possible successor board
        states based on the given state of the board"""
        sucesslist=[]
        
        for move in MOVES:
            newboard=self.board.copy()
            if newboard.move_blank(move):
                               
                b1=Board(newboard.digit_string())
                
                newstate=State(b1,self,move)
                
                sucesslist+=[newstate]
                
        return sucesslist
            
    def print_moves_to(self):
        """recursively prints the state of the board at each
        step of solivng"""
        if self.move=='init':
            print('initial state: ')
            print(self.board)
        else:    
            self.predecessor.print_moves_to()  
            print("move the blank " + self.move+":")
            print(self.board)
            
            
    
