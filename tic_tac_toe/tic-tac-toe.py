# ---------------------------------------------------------------------------- #
#*                               Tic-Tac-Toe Game                               #
# ---------------------------------------------------------------------------- #



# --------------------------------- Functions -------------------------------- #
from typing import List, Tuple, Optional
from random import randint


# Maps indices to (row, column)
index_map = {
    0: ( 0, 0 ),
    1: ( 0, 1 ),
    2: ( 0, 2 ),
    
    3: ( 1, 0 ),
    4: ( 1, 1 ),
    5: ( 1, 2 ),
    
    6: ( 2, 0 ),
    7: ( 2, 1 ),
    8: ( 2, 2 )
}

# Define solution map --> all possible winning combinations 
soln_map = [
    [0, 1, 2], 
    [3, 4, 5], 
    [6, 7, 8], 
    [0, 3, 6], 
    [1, 4, 7], 
    [2, 5, 8], 
    [0, 4, 8], 
    [2, 4, 6]
]


# Keep track of user and computer moves
user_moves = []
comp_moves = []



def DisplayBoard( board: List[ List[ str ] ], turns: int ):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    #
    border = ( "+" + "-"*7 ) * 3 + "+"
    
    print( f" --- Turn #{turns} ---" )
    ## Print formatted game board:
    print( border )
    print( "|\t|\t|\t|" )
    print( f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |" )
    print( "|\t|\t|\t|" )
    print( border )
    print( "|\t|\t|\t|" )
    print( f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |" )
    print( "|\t|\t|\t|" )
    print( border )
    print( "|\t|\t|\t|" )
    print( f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |" )
    print( "|\t|\t|\t|" )
    print( border )
    
    print()
    
def ParseMove( board: List[ List[ str ] ], move: str, user: str ):
    #
    # the function accepts the board's current status and the desired move 
    # then updates the board with the correct values. User boolean parameter dictates
    # whether the user or the computer made the move
    #
    
    if user == "user":
        if move == 1:
            board[ 0 ][ 0 ] = "O"
        elif move == 2:
            board[ 0 ][ 1 ] = "O"
        elif move == 3:
            board[ 0 ][ 2 ] = "O"    
        elif move == 4:
            board[ 1 ][ 0 ] = "O"
        elif move == 5:
            board[ 1 ][ 1 ] = "O"
        elif move == 6:
            board[ 1 ][ 2 ] = "O"
        elif move == 7:
            board[ 2 ][ 0 ] = "O"
        elif move == 8:
            board[ 2 ][ 1 ] = "O"
        elif move == 9:
            board[ 2 ][ 2 ] = "O"
        
        # Add unique moves to user_moves
        if move not in user_moves:
            user_moves.append( move - 1 )
            
    ## FIXME: shouldn't have to do the "and" logic check, use MakeListofFreeFields logical check
    # Ensure computer only takes moves that are not made by user
    elif user == "comp" and move not in user_moves:
        if move == 1:
            board[ 0 ][ 0 ] = "X"
        elif move == 2:
            board[ 0 ][ 1 ] = "X"
        elif move == 3:
            board[ 0 ][ 2 ] = "X"    
        elif move == 4:
            board[ 1 ][ 0 ] = "X"
        elif move == 5:
            board[ 1 ][ 1 ] = "X"
        elif move == 6:
            board[ 1 ][ 2 ] = "X"
        elif move == 7:
            board[ 2 ][ 0 ] = "X"
        elif move == 8:
            board[ 2 ][ 1 ] = "X"
        elif move == 9:
            board[ 2 ][ 2 ] = "X"
        
        # Add unique moves to comp_moves
        if move not in comp_moves:
            comp_moves.append( move - 1 )
            
        
        

def EnterMove( board: List[ List[ str ] ] ):
    #
    # the function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision
    #
    try:
        user_move = int( input( "Enter your move: " ).strip() )
        user_move_mapped = index_map[ user_move - 1 ]
        free_squares = MakeListOfFreeFields( board )
    except ValueError:
        print( "Invalid move" )
    else:
        if user_move_mapped in free_squares:
            ParseMove( board, user_move, "user" )
        else:
            print( "Invalid move" )
        

def MakeListOfFreeFields( board: List[ List[ str ] ] ) -> List[ tuple ]:
    #
    # the function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
    free_squares = []
    
    for row in range( len( board ) ):
        for column in range( len( board[ row ] ) ):
            if board[ row ][ column ] not in ( "O", "X" ):
                free_squares.append( ( row, column ) )
            else:
                free_squares.append( ( None, None ) )
                
    return free_squares



def VictoryFor( board: List[ List[ str ] ] ) -> Optional[ str ]:
    #
    # the function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    #

    # Check if three "X" or "O" match the soln_map
    if user_moves in soln_map:
        return "user"
    elif comp_moves in soln_map:
        return "comp"
    


def DrawMove( board: List[ List[ str ] ] ):
    #
    # the function draws the computer's move and updates the board
    #

    # Convert free_squares tuple list into a list of corresponding integers 
    free_squares = MakeListOfFreeFields( board )

    # Loop till empty square found
    while True:
        comp_move = randint( 0, 8 )
    
        # Map comp_move to ( row, column ) tuple
        comp_move_mapped = index_map[ comp_move ]
    
        if comp_move_mapped in free_squares and comp_move not in comp_moves:
            ParseMove( board, comp_move, "comp" )
            break

# ------------------------------- Main Function ------------------------------ #
def main():
    
    # Construct default board (lists are mutable so we don't have to return an updated board each time)
    board: List[ List[ str ] ] = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    
    turns = 0
    
    while True:
        turns += 1
        
        # Display board
        DisplayBoard( board, turns )
            
        # User plays their move        
        EnterMove( board )
        
        # Computer draws its move
        DrawMove( board )

        # Check if all squares already chosen
        if len( user_moves ) + len( comp_moves ) == 8:
            DisplayBoard( board, turns )
            print( "\nDRAW!" )
            break
        
        # Break if game has been won
        if VictoryFor( board ) == "user":
            DisplayBoard( board, turns )
            print( " \n<< YOU WIN! >>" )
            break
        elif VictoryFor( board ) == "comp":
            DisplayBoard( board, turns )
            print( " \n<< YOU LOST TO A RANDOM NUMBER GENERATOR! >> " )
            break
        




# -------------------------------- Run Program ------------------------------- #
if __name__ == "__main__":
    main()