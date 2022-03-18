#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: brandon bouley
# email: bbouley@bu.edu


# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        indexcount=0
        
        for r in range(3):
            for c in range(3):
                
                
                self.tiles[r][c]=digitstr[indexcount]
                
                if self.tiles[r][c]=='0':
                    self.blank_r=r
                    self.blank_c=c
                
                indexcount+=1
                

    
    def __repr__(self):
        """string representation of Board object where the blank
        is represented by character '_' """
        newstr=''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c]=='0' and c==2:
                    newstr+='_ \n'
                elif self.tiles[r][c]=='0':
                    newstr+='_ '
                elif c==2:
                    newstr+=self.tiles[r][c]+' \n'
                else:
                    newstr+=self.tiles[r][c]+' '
        return newstr
    
    def move_blank(self,direction):
        """moves the blank depending on variable direction,
        updates object self"""
        
        moves= ['up', 'down', 'left', 'right']
        if direction not in moves:
            return False
        
        if direction=='up':
            newblank_r=self.blank_r-1
            newblank_c=self.blank_c
        elif direction=='down':
            newblank_r=self.blank_r+1
            newblank_c=self.blank_c
        elif direction=='left':
            newblank_r=self.blank_r
            newblank_c=self.blank_c-1
        elif direction=='right':
            newblank_r=self.blank_r
            newblank_c=self.blank_c+1
        
        if newblank_c<0 or newblank_c>2 or newblank_r<0 \
           or newblank_r>2:
           # Checks if the new position determined by parameter direction causes the array to overflow
               
           return False
       
        else:
            movednumber=self.tiles[newblank_r][newblank_c]
            self.tiles[newblank_r][newblank_c]='0'
            self.tiles[self.blank_r][self.blank_c]=movednumber
            
            self.blank_r=newblank_r
            self.blank_c=newblank_c
            
            return True
       
    def digit_string(self):
        """returns new digitstring, based on the current state 
        of the board"""
        digitstring=''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                digitstring+=self.tiles[r][c]
        return digitstring
       
    def copy(self):
        """creates a deep copy of board self"""
        newBoard= Board(self.digit_string())
        
        return newBoard
    
    def num_misplaced(self):
        """returns the number of tiles in the wrong spot, 
        minus the blank space"""
        misplaced=0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c]!=GOAL_TILES[r][c] \
                    and self.tiles[r][c]!='0':
                    misplaced+=1
        
        return misplaced
        
    def misplaced_rowcol(self):
        """returns the combined number of items in the wrong
        row and items in the wrong column"""
        rowcolval_init=[]
        rowcolval_goal=[]
        misplaced_row=0
        misplaced_col=0

        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                # Creates two lists, one which reflects the current state of the board
                # and another which reflects the goal state of the board.
                rowcolval_init+=[[r,c,self.tiles[r][c]]]
                rowcolval_goal+=[[r,c,GOAL_TILES[r][c]]]
       
        for i in rowcolval_init:
            for j in rowcolval_goal:
                # Compares the current state of the rows to the goal state.
                if i[-1] == j[-1] and i[0] != j[0] \
                    and i[-1]!='0':
                        
                    misplaced_row+=1
       
        for i in rowcolval_init: 
            for j in rowcolval_goal:
                # Compares the current state of the columns to the goal state.
                if i[-1] == j[-1] and i[1] != j[1]\
                    and i[-1]!='0':
                        
                    misplaced_col+=1
        # Note: with this method, a tile in the wrong row AND column will be 
        # weighted twice as much as a tile in the wrong row but correct column
        # and vice versa.
        
        return misplaced_col+misplaced_row
            
                
        
    
    def __eq__(self,other):
        """checks if both tile elements are equal"""
        return self.tiles==other.tiles
    
                
        
                
            
