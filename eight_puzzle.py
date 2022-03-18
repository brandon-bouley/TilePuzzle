#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: brandon bouley
# email: bbouley@bu.edu


from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            
    
def process_file(filename, algorithm, param):
    
    """systematically processes all digitstrings in a textfile
    with given algoritim and parameters, determines moves and
    states tested for each solution along with averages for the
    whole file."""
    
    file = open(filename, 'r')
    text=file.read()
    file.close()
    
    totalstates=0
    totalmoves=0
    puzzlescount=0
    statecount=0
    movescount=0
    proof=False
        
    lines=text.split('\n')
        
    for i in lines:
        
        init_board = Board(i)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        
        
        print(i+":", end=" ")
        soln = None
        try:
            soln = searcher.find_solution(init_state)
        except KeyboardInterrupt:
            print('search terminated, ', end='')
        if soln == None:
            print("no solution")
        else:
            proof=True #proof that there is at least 1 solution
            print(str(soln.num_moves)+" moves, " \
              +str(searcher.num_tested)+" states tested")
        
            totalstates+=searcher.num_tested
            statecount+=1
            totalmoves+=soln.num_moves
            movescount+=1
            puzzlescount+=1
    if proof:
        
        avgmoves=totalmoves/movescount
        avgstates=totalstates/statecount
   
        print()
        print("solved "+str(puzzlescount)+" puzzles")
        print("averages: "+str(avgmoves)+" moves, "+str(avgstates)+" states tested")
        
    
