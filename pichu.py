#!/usr/bin/env python
"""
This is an implementation of chess using minimax and alpha-beta pruning
Author : Hasika Mahtta
"""
import copy
import sys
import time

#Three arguments are taken player, state and time_limit.    
player=str(sys.argv[1])
state=str(sys.argv[2])
time_limit=int(sys.argv[3])

#Evaluation Function
def count(b):

    P_count=sum(x.count('P') for x in b)
    R_count=sum(x.count('R') for x in b)
    N_count = sum(x.count('N') for x in b)
    Q_count = sum(x.count('Q') for x in b)
    K_count = sum(x.count('K') for x in b)
    p_count = sum(x.count('p') for x in b)
    r_count = sum(x.count('r') for x in b)
    n_count = sum(x.count('n') for x in b)
    k_count = sum(x.count('k') for x in b)
    b_count = sum(x.count('b') for x in b)
    q_count= sum(x.count('q') for x in b)
    B_count = sum(x.count('B') for x in b)
    eval=(1*float(P_count-p_count)+3*float(N_count-n_count)+3*float(B_count-b_count)+5*float(R_count-r_count)
        +9*float(Q_count-q_count)+200*float(K_count-k_count))
    if self_piece == 'w':
        return eval
    elif self_piece == 'b':
       return -1*eval
#Function for printing all the possible moves if the piece is White.
#WHEN ALL PIECES ARE WHITE
#parakeet moves
def piece(board,index):
    moves= []
    i,j=index
    #if the piece is capital 'P'
    #normal move
    if board[i][j]=='P':
        if i<7 and board[i + 1][j] == '.':
            board1 = copy.deepcopy(board)
            if i != 6:
               board1[i + 1][j] = 'P'
            else:
               board1[i + 1][j] = 'Q' 
            board1[i][j] = '.'
            moves.append((board1,count(board1)))
    #return moves
    if board[i][j]=='P' and i==1:
        if  board[i + 2][j] == '.' and board[i + 1][j] == '.':
            board1 = copy.deepcopy(board)
            board1[i + 2][j] = 'P'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

    #right diagonal opponent
    # if opponent is on right diagonal
        if i < 7 and j < 7 and board[i + 1][j + 1] in 'rnbkqp':
               board1=copy.deepcopy(board)
               if i != 6:
                  board1[i + 1][j + 1] = 'P'
               else:
                  board1[i + 1][j + 1] = 'Q' 
               board1[i][j] = '.'
               moves.append((board1,count(board1)))
               return moves
        # if opponent is on left diagonal
        if i < 7 and j != 0 and board[i + 1][j - 1] in 'rnbkqp':
           board1 = copy.deepcopy(board)
           if i != 6:
              board1[i + 1][j - 1] = 'P'
           else:
              board1[i + 1][j - 1] = 'Q' 
           board1[i][j] = '.'
           moves.append((board1,count(board1)))
           return moves

#--------------------------------------------------------------------------------------------------------------------------------------

#Kingfisher moves- If king is capital K
#king down
    if board[i][j]=='K':
       if i<7 and board[i + 1][j] == '.':
            board1 = copy.deepcopy(board)
            board1[i + 1][j] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

       #opponent moves
       if i<7 and board[i + 1][j] in "rnbqkp":
        board1=copy.deepcopy(board)
        board1[i + 1][j] = 'K'
        board1[i][j] = '.'
        moves.append((board1,count(board1)))

#kingup-regular move
       if i!=0  and board[i-1][j] == '.':
            board1=copy.deepcopy(board)
            board1[i-1][j] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

        # opponent moves
       if i!=0  and  board[i - 1][j] in "rnbqkp":
            board1 = copy.deepcopy(board)
            board1[i - 1][j] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#Kingfisherleft - regular moves
       if j!=0  and board[i][j-1] == '.':
            board1=copy.deepcopy(board)
            board1[i][j-1] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

        # opponent moves
       if j!=0  and  board[i][j-1] in "rnbqkp":
            board1 = copy.deepcopy(board)
            board1[i][j-1] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#Kingfisherright - regular moves
       if j<7 and board[i][j+1] == '.':
            board1=copy.deepcopy(board)
            board1[i][j+1] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

        # opponent moves
       if  j<7  and  board[i][j+1] in "rnbqkp":
            board1 = copy.deepcopy(board)
            board1[i][j+1] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#Kingfisher left upper diagonal - regular moves
       if i!=0 and j!=0  and board[i-1][j-1] == '.':
            board1=copy.deepcopy(board)
            board1[i-1][j-1] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

        # opponent moves
       if  i!=0 and j!=0  and  board[i-1][j-1] in "rnbqkp":
            board1 = copy.deepcopy(board)
            board1[i-1][j-1] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#Kingfisher right upper diagonal - regular moves
       if i!=0 and j<7  and board[i-1][j+1] == '.':
            board1=copy.deepcopy(board)
            board1[i-1][j+1] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

        # opponent moves
       if  i!=0  and j<7 and  board[i-1][j+1] in "rnbqkp":
            board1 = copy.deepcopy(board)
            board1[i-1][j+1] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#Kingfisher left lower diagonal - regular moves
       if j!=0  and i<7 and board[i+1][j-1] == '.':
            board1=copy.deepcopy(board)
            board1[i+1][j-1] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

        # opponent moves
       if j!=0  and i<7 and board[i+1][j-1] in "rnbqkp":
            board1 = copy.deepcopy(board)
            board1[i+1][j-1] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#Kingfisher right lower diagonal - regular moves
       if  j<7 and i<7 and board[i+1][j+1] == '.':
            board1=copy.deepcopy(board)
            board1[i+1][j+1] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

        # opponent moves
       if j<7 and i<7 and board[i+1][j+1] in "rnbqkp":
            board1 = copy.deepcopy(board)
            board1[i+1][j+1] = 'K'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Robin Moves
#When Robin is capital 'R'- white rook
#When Robin moves all left
    if board[i][j]=='R':
       for x in range(j-1,-1,-1):
           if board[i][x] not in'.':
               if board[i][x] in "rnbqkp":
                   board1=copy.deepcopy(board)
                   board1[i][x]='R'
                   board1[i][j]='.'
                   moves.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[i][x]='R'
           board1[i][j]='.'
           moves.append((board1,count(board1)))

#When Robin moves all right
    if board[i][j]=='R':
       for x in range(j+1,8):
           if board[i][x] not in'.':
               if board[i][x] in "rnbqkp":
                   board1=copy.deepcopy(board)
                   board1[i][x]='R'
                   board1[i][j]='.'
                   moves.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[i][x]='R'
           board1[i][j]='.'
           moves.append((board1,count(board1)))

#When Robin moves all up
       for x in range(i-1,-1,-1):
           if board[x][j] not in'.':
               if board[x][j] in "rnbqkp":
                   board1=copy.deepcopy(board)
                   board1[x][j]='R'
                   board1[i][j]='.'
                   moves.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[x][j]='R'
           board1[i][j]='.'
           moves.append((board1,count(board1)))

#When Robin moves all down
       for x in range(i+1,8):
           if board[x][j] not in'.':
               if board[x][j] in "rnbqkp":
                   board1=copy.deepcopy(board)
                   board1[x][j]='R'
                   board1[i][j]='.'
                   moves.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[x][j]='R'
           board1[i][j]='.'
           moves.append((board1,count(board1)))


#-------------------------------------------------------------------------------------------------------------------
#NIGHT MOVES
#When night is capital 'N'= White
#When night can move 2steps left-upper
    if board[i][j]=='N':
       if i>1 and j!=0 and board[i-2][j-1]=='.':
           board1=copy.deepcopy(board)
           board1[i-2][j-1]='N'
           board1[i][j]='.'
           moves.append((board1,count(board1)))
       #opponent moves
       if i>1  and j!=0 and board[i-2][j-1] in "rnbqkp":
           board1=copy.deepcopy(board)
           board1[i-2][j-1]='N'
           board1[i][j]='.'
           moves.append((board1,count(board1)))

#When night can move 1 step left-upper
       if i>1 and j>1 and board[i-1][j-2]=='.':
           board1=copy.deepcopy(board)
           board1[i-1][j-2]='N'
           board1[i][j]='.'
           moves.append((board1,count(board1)))
       # opponent moves
       if i > 1 and j > 1 and board[i - 1][j-2] in "rnbqkp":
           board1 = copy.deepcopy(board)
           board1[i - 1][j -2] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))

#When night can move 2 steps right-upper
       if  i>1 and j<7 and board[i - 2][j + 1] == '.':
           board1 = copy.deepcopy(board)
           board1[i - 2][j + 1] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))
        # opponent moves
       if i>1 and j < 7 and board[i - 2][j + 1] in "rnbqkp":
           board1 = copy.deepcopy(board)
           board1[i - 2][j + 1] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))

# When night can move 1 step right-upper
       if i!=0 and j < 6 and board[i - 1][j + 2] == '.':
           board1 = copy.deepcopy(board)
           board1[i -1 ][j + 2] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))
           # opponent moves
       if i!=0 and j < 6 and board[i-1][j + 2] in "rnbqkp":
           board1 = copy.deepcopy(board)
           board1[i - 1][j + 2] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))

#When night can move 2 steps right-lower
       if  i<6 and j<7 and board[i + 2][j + 1] == '.':
           board1 = copy.deepcopy(board)
           board1[i + 2][j + 1] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))
        # opponent moves
       if i<6 and j<7 and board[i + 2][j + 1] in "rnbqkp":
           board1 = copy.deepcopy(board)
           board1[i + 2][j + 1] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))

#When night can move 1 step right-lower
       if  i<7 and j<6 and board[i + 1][j + 2] == '.':
           board1 = copy.deepcopy(board)
           board1[i + 1][j + 2] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))
        # opponent moves
       if i<7 and j<6 and board[i + 1][j + 2] in "rnbqkp":
           board1 = copy.deepcopy(board)
           board1[i + 1][j + 2] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))

#When night can move 2 steps left-lower
       if  j!=0 and i<6 and board[i + 2][j - 1] == '.':
           board1 = copy.deepcopy(board)
           board1[i + 2][j - 1] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))
        # opponent moves
       if  j!=0 and i<6 and board[i + 2][j - 1] in "rnbqkp":
           board1 = copy.deepcopy(board)
           board1[i + 2][j - 1] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))

#When night can move 1 step left-lower
       if  j>1 and i<7 and board[i + 1][j - 2] == '.':
           board1 = copy.deepcopy(board)
           board1[i + 1][j - 2] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))
        # opponent moves
       if  j>1 and i<7 and board[i + 1][j - 2] in "rnbqkp":
           board1 = copy.deepcopy(board)
           board1[i + 1][j - 2] = 'N'
           board1[i][j] = '.'
           moves.append((board1,count(board1)))
#==========================================================================================================================================================
#Bluejay moves
#When Bluejay is capital 'B'= white piece
#When Bluejay can move all left upper diagonal
    if board[i][j]=='B':
        for x,y in zip(range(i - 1, -1, -1),range(j-1,-1,-1)):
            if board[x][y] not in '.':
                if board[x][y] in "rnbqkp":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'B'
                    board1[i][j] = '.'
                    moves.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'B'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#When Bluejay can move all right upper diagonal
    if board[i][j]=='B':
        for x,y in zip(range(i-1,-1,-1),range(j+1,8)):
            if board[x][y] not in '.':
                if board[x][y] in "rnbqkp":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'B'
                    board1[i][j] = '.'
                    moves.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'B'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#When Bluejay can move all right lower diagonal
    if board[i][j]=='B':
        for x,y in zip(range(i+1,8),range(j+1,8)):
            if board[x][y] not in '.':
                if board[x][y] in "rnbqkp":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'B'
                    board1[i][j] = '.'
                    moves.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'B'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#When Bluejay can move all left lower diagonal
    if board[i][j]=='B':
        for x,y in zip(range(i+1,8),range(j-1,-1,-1)):
            if board[x][y] not in '.':
                if board[x][y] in "rnbqkp":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'B'
                    board1[i][j] = '.'
                    moves.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'B'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#====================================================================================================================================================
#QUEEN MOVES
#When Quetzal is capital 'Q'
#When Quetzal moves all left
    if board[i][j]=='Q':
       for x in range(j-1,-1,-1):
           if board[i][x] not in'.':
               if board[i][x] in "rnbqkp":
                   board1=copy.deepcopy(board)
                   board1[i][x]='Q'
                   board1[i][j]='.'
                   moves.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[i][x]='Q'
           board1[i][j]='.'
           moves.append((board1,count(board1)))

#When Quetzal moves all right
       for x in range(j+1,8):
           if board[i][x] not in'.':
               if board[i][x] in "rnbqkp":
                   board1=copy.deepcopy(board)
                   board1[i][x]='Q'
                   board1[i][j]='.'
                   moves.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[i][x]='Q'
           board1[i][j]='.'
           moves.append((board1,count(board1)))

#When Quetzal moves all up
       for x in range(i-1,-1,-1):
           if board[x][j] not in'.':
               if board[x][j] in "rnbqkp":
                   board1=copy.deepcopy(board)
                   board1[x][j]='Q'
                   board1[i][j]='.'
                   moves.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[x][j]='Q'
           board1[i][j]='.'
           moves.append((board1,count(board1)))

#When Quetzal moves all down
       for x in range(i+1,8):
           if board[x][j] not in'.':
               if board[x][j] in "rnbqkp":
                   board1=copy.deepcopy(board)
                   board1[x][j]='Q'
                   board1[i][j]='.'
                   moves.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[x][j]='Q'
           board1[i][j]='.'
           moves.append((board1,count(board1)))

#When Quetzal moves all left upper diagonal
       for x,y in zip(range(i - 1, -1, -1),range(j-1,-1,-1)):
            if board[x][y] not in '.':
                if board[x][y] in "rnbqkp":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'Q'
                    board1[i][j] = '.'
                    moves.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'Q'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#When Quetzal can move all right upper diagonal
       for x,y in zip(range(i-1,-1,-1),range(j+1,8)):
            if board[x][y] not in '.':
                if board[x][y] in "rnbqkp":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'Q'
                    board1[i][j] = '.'
                    moves.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'Q'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#When Quetzal can move all right lower diagonal
       for x,y in zip(range(i+1,8),range(j+1,8)):
            if board[x][y] not in '.':
                if board[x][y] in "rnbqkp":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'Q'
                    board1[i][j] = '.'
                    moves.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'Q'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))

#When Quetzal can move all left lower diagonal
       for x,y in zip(range(i+1,8),range(j-1,-1,-1)):
            if board[x][y] not in '.':
                if board[x][y] in "rnbqkp":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'Q'
                    board1[i][j] = '.'
                    moves.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'Q'
            board1[i][j] = '.'
            moves.append((board1,count(board1)))
    return moves
#-------------------------------------------------------------------------------------------------------------------------------------------------
#When all the pieces are black
def piece1(board, index):
    moves1 = []
    i, j = index
#if parakket is small 'p'
    if board[i][j]=='p':
        if i!=0 and board[i - 1][j] == '.':
           board1 = copy.deepcopy(board)
           if i !=1:
              board1[i - 1][j] = 'p'
           else:
              board1[i - 1][j] = 'q' 
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))
           
    if board[i][j]=='p' and i == 6:
        if  board[i - 2][j] == '.' and board[i - 1][j] == '.':
           board1 = copy.deepcopy(board)
           board1[i - 2][j] = 'p'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))

    #right diagonal opponent
    # if opponent is on right diagonal
        if i!=0 and j < 7 and board[i-1][j+1] in 'RNBQKP':
           board1=copy.deepcopy(board)
           if i != 1:
              board1[i - 1][j + 1] = 'p'
           else:
              board1[i - 1][j + 1] = 'q' 
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))

    # if opponent is on left diagonal
        if j!=0 and i!=0  and board[i - 1][j - 1] in 'RNBQKP':
           board1 = copy.deepcopy(board)
           if i != 1:
              board1[i - 1][j - 1] = 'p'
           else:
              board1[i - 1][j - 1] = 'q' 
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))

#============================================================================================================================================================
#Kingfisher moves- If Kingfisher is small 'k'
#Kingfisherdown
    if board[i][j]=='k':
       if i<7 and board[i + 1][j] == '.':
           board1 = copy.deepcopy(board)
           board1[i + 1][j] = 'k'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))

        #opponent moves
       if i<7 and board[i + 1][j] in "RNBKQP":
        board1=copy.deepcopy(board)
        board1[i + 1][j] = 'k'
        board1[i][j] = '.'
        moves1.append((board1,count(board1)))

#Kingfisherup-regular move
       if i!=0  and board[i-1][j] == '.':
            board1=copy.deepcopy(board)
            board1[i-1][j] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

        # opponent moves
       if i!=0  and  board[i - 1][j] in "RNBKQP":
            board1 = copy.deepcopy(board)
            board1[i - 1][j] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))
   # return moves

#Kingfisher_left - regular moves
       if j!=0  and board[i][j-1] == '.':
            board1=copy.deepcopy(board)
            board1[i][j-1] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

        # opponent moves
       if j!=0  and  board[i][j-1] in "RNBKQP":
            board1 = copy.deepcopy(board)
            board1[i][j-1] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#Kingfsher_right - regular moves
       if j<7 and board[i][j+1] == '.':
            board1=copy.deepcopy(board)
            board1[i][j+1] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

        # opponent moves
       if  j<7  and  board[i][j+1] in "RNBKQP":
            board1 = copy.deepcopy(board)
            board1[i][j+1] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#Kingfsher left upper diagonal - regular moves
       if i!=0 and j!=0  and board[i-1][j-1] == '.':
            board1=copy.deepcopy(board)
            board1[i-1][j-1] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

        # opponent moves
       if  i!=0 and j!=0  and  board[i-1][j-1] in "RNBKQP":
            board1 = copy.deepcopy(board)
            board1[i-1][j-1] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#Kingfsher right upper diagonal - regular moves
       if i!=0 and j<7  and board[i-1][j+1] == '.':
            board1=copy.deepcopy(board)
            board1[i-1][j+1] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

        # opponent moves
       if  i!=0  and j<7 and  board[i-1][j+1] in "RNBKQP":
            board1 = copy.deepcopy(board)
            board1[i-1][j+1] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#Kingfsher left lower diagonal - regular moves
       if j!=0  and i<7 and board[i+1][j-1] == '.':
            board1=copy.deepcopy(board)
            board1[i+1][j-1] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

        # opponent moves
       if j!=0  and i<7 and board[i+1][j-1] in "RNBKQP":
            board1 = copy.deepcopy(board)
            board1[i+1][j-1] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#Kingfsher right lower diagonal - regular moves
       if  j<7 and i<7 and board[i+1][j+1] == '.':
            board1=copy.deepcopy(board)
            board1[i+1][j+1] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

        # opponent moves
       if j<7 and i<7 and board[i+1][j+1] in "RNBKQP":
            board1 = copy.deepcopy(board)
            board1[i+1][j+1] = 'k'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#MOVES FOR SMALL (black) ROOK 'r'-----------------------------------------------------------------------
#When Robin moves all left
    if board[i][j]=='r':
       for x in range(j-1,-1,-1):
           if board[i][x] not in'.':
               if board[i][x] in "RNBQKP":
                   board1=copy.deepcopy(board)
                   board1[i][x]='r'
                   board1[i][j]='.'
                   moves1.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[i][x]='r'
           board1[i][j]='.'
           moves1.append((board1,count(board1)))

#When Robin moves all right
       for x in range(j+1,8):
           if board[i][x] not in'.':
               if board[i][x] in "RNBQKP":
                   board1=copy.deepcopy(board)
                   board1[i][x]='r'
                   board1[i][j]='.'
                   moves1.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[i][x]='r'
           board1[i][j]='.'
           moves1.append((board1,count(board1)))

#When Robin moves all up
       for x in range(i-1,-1,-1):
           if board[x][j] not in'.':
               if board[x][j] in "RNBQKP":
                   board1=copy.deepcopy(board)
                   board1[x][j]='r'
                   board1[i][j]='.'
                   moves1.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[x][j]='r'
           board1[i][j]='.'
           moves1.append((board1,count(board1)))

#When Robin moves all down
       for x in range(i+1,8):
           if board[x][j] not in'.':
               if board[x][j] in "RNBQKP":
                   board1=copy.deepcopy(board)
                   board1[x][j]='r'
                   board1[i][j]='.'
                   moves1.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[x][j]='r'
           board1[i][j]='.'
           moves1.append((board1,count(board1)))

#When Night is small 'n' = Black n
#When night can move 2steps left-upper
    if board[i][j]=='n':
       if i>1 and j!=0 and board[i-2][j-1]=='.':
           board1=copy.deepcopy(board)
           board1[i-2][j-1]='n'
           board1[i][j]='.'
           moves1.append((board1,count(board1)))
       #opponent moves
       if i>1  and j!=0 and board[i-2][j-1] in "RNBQKP":
           board1=copy.deepcopy(board)
           board1[i-2][j-1]='n'
           board1[i][j]='.'
           moves1.append((board1,count(board1)))

#When night can move 1 step left-upper
       if i>1 and j>1 and board[i-1][j-2]=='.':
           board1=copy.deepcopy(board)
           board1[i-1][j-2]='n'
           board1[i][j]='.'
           moves1.append((board1,count(board1)))
       # opponent moves
       if i > 1 and j > 1 and board[i - 1][j-2] in "RNBQKP":
           board1 = copy.deepcopy(board)
           board1[i - 1][j -2] = 'N'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))

#When night can move 2 steps right-upper
       if  i>1 and j<7 and board[i - 2][j + 1] == '.':
           board1 = copy.deepcopy(board)
           board1[i - 2][j + 1] = 'n'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))
        # opponent moves
       if i>1 and j < 7 and board[i - 2][j + 1] in "RNBQKP":
           board1 = copy.deepcopy(board)
           board1[i - 2][j + 1] = 'n'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))

# When night can move 1 step right-upper
       if i!=0 and j < 6 and board[i - 1][j + 2] == '.':
           board1 = copy.deepcopy(board)
           board1[i -1 ][j + 2] = 'n'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))
           # opponent moves
       if i!=0 and j < 6 and board[i-1][j + 2] in "RNBQKP":
           board1 = copy.deepcopy(board)
           board1[i - 1][j + 2] = 'n'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))

#When night can move 2 steps right-lower
       if  i<6 and j<7 and board[i + 2][j + 1] == '.':
           board1 = copy.deepcopy(board)
           board1[i + 2][j + 1] = 'n'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))
        # opponent moves
       if i<6 and j<7 and board[i + 2][j + 1] in "RNBQKP":
           board1 = copy.deepcopy(board)
           board1[i + 2][j + 1] = 'n'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))

#When night can move 1 step right-lower
       if  i<7 and j<6 and board[i + 1][j + 2] == '.':
           board1 = copy.deepcopy(board)
           board1[i + 1][j + 2] = 'n'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))
        # opponent moves
       if i<7 and j<6 and board[i + 1][j + 2] in "RNBQKP":
           board1 = copy.deepcopy(board)
           board1[i + 1][j + 2] = 'n'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))

#When night can move 2 steps left-lower
       if  j!=0 and i<6 and board[i + 2][j - 1] == '.':
           board1 = copy.deepcopy(board)
           board1[i + 2][j - 1] = 'n'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))
        # opponent moves
       if  j!=0 and i<6 and board[i + 2][j - 1] in "RNBQKP":
           board1 = copy.deepcopy(board)
           board1[i + 2][j - 1] = 'n'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))

#When night can move 1 step left-lower
       if  j>1 and i<7 and board[i + 1][j - 2] == '.':
           board1 = copy.deepcopy(board)
           board1[i + 1][j - 2] = 'n'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))
        # opponent moves
       if  j>1 and i<7 and board[i + 1][j - 2] in "RNBQKP":
           board1 = copy.deepcopy(board)
           board1[i + 1][j - 2] = 'n'
           board1[i][j] = '.'
           moves1.append((board1,count(board1)))
#======================================================================================================================
#When Bluejay is capital 'b'= Black piece
#When Bluejay can move all left upper diagonal
    if board[i][j]=='b':
        for x,y in zip(range(i - 1, -1, -1),range(j-1,-1,-1)):
            if board[x][y] not in '.':
                if board[x][y] in "RNBKQP":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'b'
                    board1[i][j] = '.'
                    moves1.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'b'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#When Bluejay can move all righupper diagonal
    if board[i][j]=='b':
        for x,y in zip(range(i-1,-1,-1),range(j+1,8)):
            if board[x][y] not in '.':
                if board[x][y] in "RNBKQP":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'b'
                    board1[i][j] = '.'
                    moves1.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'b'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#When Bluejay can move all right lower diagonal
    if board[i][j]=='b':
        for x,y in zip(range(i+1,8),range(j+1,8)):
            if board[x][y] not in '.':
                if board[x][y] in "RNBKQP":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'b'
                    board1[i][j] = '.'
                    moves1.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'b'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#When Bluejay can move all left lower diagonal
    if board[i][j]=='b':
        for x,y in zip(range(i+1,8),range(j-1,-1,-1)):
            if board[x][y] not in '.':
                if board[x][y] in "RNBKQP":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'b'
                    board1[i][j] = '.'
                    moves1.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'b'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#=====================================================================================================================================================================
#When the Quetzal is small 'q' = black Quetzal
#When Quetzal moves all left
    if board[i][j]=='q':
       for x in range(j-1,-1,-1):
           if board[i][x] not in'.':
               if board[i][x] in "RNBKQP":
                   board1=copy.deepcopy(board)
                   board1[i][x]='q'
                   board1[i][j]='.'
                   moves1.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[i][x]='q'
           board1[i][j]='.'
           moves1.append((board1,count(board1)))

#When Quetzal moves all right
       for x in range(j+1,8):
           if board[i][x] not in'.':
               if board[i][x] in "RNBKQP":
                   board1=copy.deepcopy(board)
                   board1[i][x]='q'
                   board1[i][j]='.'
                   moves1.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[i][x]='q'
           board1[i][j]='.'
           moves1.append((board1,count(board1)))

#When Quetzal moves all up
       for x in range(i-1,-1,-1):
           if board[x][j] not in'.':
               if board[x][j] in "RNBKQP":
                   board1=copy.deepcopy(board)
                   board1[x][j]='q'
                   board1[i][j]='.'
                   moves1.append((board1,count(board1)))
               break
           board1=copy.deepcopy(board)
           board1[x][j]='q'
           board1[i][j]='.'
           moves1.append((board1,count(board1)))

#When Quetzal moves all down
       for x in range(i+1,8):
           if board[x][j] not in'.':
               if board[x][j] in "RNBKQP":
                   board1=copy.deepcopy(board)
                   board1[x][j]='q'
                   board1[i][j]='.'
                   moves1.append((board1,count(board1))),
               break
           board1=copy.deepcopy(board)
           board1[x][j]='q'
           board1[i][j]='.'
           moves1.append((board1,count(board1)))

#When Quetzal moves all left upper diagonal
       for x,y in zip(range(i - 1, -1, -1),range(j-1,-1,-1)):
            if board[x][y] not in '.':
                if board[x][y] in "RNBKQP":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'q'
                    board1[i][j] = '.'
                    moves1.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'q'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#When Quetzal can move all right upper diagonal
       for x,y in zip(range(i-1,-1,-1),range(j+1,8)):
            if board[x][y] not in '.':
                if board[x][y] in "RNBKQP":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'q'
                    board1[i][j] = '.'
                    moves1.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'q'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#When Quetzal can move all right lower diagonal
       for x,y in zip(range(i+1,8),range(j+1,8)):
            if board[x][y] not in '.':
                if board[x][y] in "RNBKQP":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'q'
                    board1[i][j] = '.'
                    moves1.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'q'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))

#When Quetzal can move all left lower diagonal
       for x,y in zip(range(i+1,8),range(j-1,-1,-1)):
            if board[x][y] not in '.':
                if board[x][y] in "RNBKQP":
                    board1 = copy.deepcopy(board)
                    board1[x][y] = 'q'
                    board1[i][j] = '.'
                    moves1.append((board1,count(board1)))
                break
            board1 = copy.deepcopy(board)
            board1[x][y] = 'q'
            board1[i][j] = '.'
            moves1.append((board1,count(board1)))
    return moves1
#=====================================================================================================================
#printing white moves
# for i in range(0,8):
#      for j in range(0,8):
#          P=piece(initial_board,(i, j))
#          for x in P:
#             print x
#
#  #printing black moves
# for i in range(0,8):
#      for j in range(0,8):
#          P1=piece1(initial_board, (i, j))
#          for t in P1:
#             print t
#successors should return a list of tuples
#As helped from Prof. Crandall
#Successor function
def successors(board,player):
    l1 = []
    for i in range(0,8):
        for j in range(0,8):
            if player=='w':
                p=piece(board,(i,j))
                l1+=p
            if player=='b':
                p1=piece1(board,(i,j))
                l1+= p1
    return l1
#successors(initial_board,'white')

#Terminal State
def Terminal(S,D):
    if D == 0:
        return True
    count_kings = 0
    for i in range(0,8):
        for j in range(0,8):
            if 'K' in S[0][i][j] or 'k' in S[0][i][j]:
                count_kings = count_kings + 1                    
    if D != 0 and count_kings == 2:
        return False
    else:    
        return True

#Discussed with Larry of how to implement the alpha beta algorithm as sited from aima-python git.
#Understood the pseudo code from this source and then implemented it.
#Alpha-beta pruning applied minimax algorithm

def alpha_beta_decision(S,player, d):
    curr_best=-10000000
    # this is the start  board, it is a list of lists representing the board
    if time.time()<current_time+time_limit:
	    for s in successors(S,player):
        	r=Max_value(s,-1000000,+1000000,player,d,s[0])
	        if r > curr_best:
        	    curr_best = r
		    best_state = s[0]
            # TODO: Print out current board you passed in
            print 'best board is:'
	   # print printable_board2(best_state)
	    print printable_board(best_state)

            	
#Max function
def Max_value(board,alpha,beta,player,D,cb):
    # The board is [board, eval]
    if Terminal(board,D):
        return board[1]
    value = -100000000000
    #  Alternate player
    if player == "w":
       player = "b"
    else:
        player = "w"
    if time.time()<current_time+time_limit:
     for s in successors(board[0],player):
        value=max(value,Min_value(s,alpha,beta,player, D-1,cb)) # TODO: Alternate player
        if value >= beta:
            if value >beta:
                pass
            return value
        alpha = max(alpha, value)
     return value
    else:
	sys.exit(0)

#Min Function
def Min_value(board,alpha,beta,player,D,cb):
    if Terminal(board,D):
        return board[1]
    value = +100000000000
    if player == "w":
        player = "b"
    else:
        player = "w"
    if time.time()<current_time+time_limit:
     for s in successors(board[0],player):
        value=min(value,Max_value(s,alpha,beta,player, D-1,cb)) # TODO: Alternate player
        if value <= alpha:
            return value
        beta = min(beta, value)
     return value
    else:
	sys.exit(0)
     # s1=successors(S,'white')
     # print s1
     # l=[]
     # for x in s1:
     #     l.append(x[1])
     # print l
     # for x in l1:
     #  return  max(Min_Value(s1,-float(inf),+float(inf)))
# The time you pass in should be related to the depth

#Printing board in the form of string.
def printable_board(board):
    final = ''
    for i in list(range(0,8)):
        for j in list(range(0,8)):
            final = final + board[i][j]
    return final

#Main Program
initial_board_input = state
self_piece = player
initial_board=[]

k=0
for i in list(range(0,8)):
    sub_row = []
    for j in list(range(0,8)):
        sub_row.append(initial_board_input[k])
        k=k+1
    initial_board.append(sub_row)

#Board in the form of list of lists
def printable_board2(board):
    return "\n".join([ " ".join([ col for col in row ]) for row in board])


current_time = time.time()

#Running the program within thr given time limit
depth=1
while(time.time()<current_time+time_limit):
	alpha_beta_decision(initial_board,player,depth)
	depth = depth+1

