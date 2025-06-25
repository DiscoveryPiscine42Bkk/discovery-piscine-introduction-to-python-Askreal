import re
import math
    
    
def check_borad(num):
    if math.sqrt(num) == int(math.sqrt(num)):
        return True
    else :
        return False
    
def check_king(board):
    # print('checking for the king')
    state = re.findall('K',board)
    
    if (len(state)) == 1:
        return True
    else:
        print(f'Your borad have no King like you have no heart')
        return False
    
def pawn(board , x , y ,size_row):
    # y-1 and x-1 , x+1 
    if y+1 > size_row:
        board[x-1][y+1] = 'P' 
    if y-1 < size_row:
        board[x-1][y-1] = 'P'
    return board

def rook(board , x , y ,size_row):
    enemy = ['K','P','B','R','Q']
    # go up
    i = 1
    while x-i > 0: 
        if board[x-i][y] in enemy:
            break
        board[x-i][y] = 'R'
        i += 1
        
    # go down
    i = 1
    while x+i < size_row:
        if board[x+i][y] in enemy:
            break
        print(x+i)
        print(f'x+i = {x+i}')
        board[x+i][y] = 'R'
        i += 1

    # go right
    i = 1
    while y+i < size_row : 
        if board[x][y+i] in enemy:
            break
        board[x][y+i] = 'R' 
        i += 1
        
    # go left
    i = 1
    while y+i > 0 : 
        if board[x][y-i] in enemy:
            break
        board[x][y-i] = 'R'
        i += 1
    for i in board:
        for j in i:
            print(j , end='')
        print('\n')
    (board)
    
def checkmate(board):
    board = board.upper()
    charactor = ['K','P','B','R','Q','.']
    
    check_king(board)
    
    # Checking the borad is square or not
    new_borad = [x for x in board if x in charactor]
    if not check_borad(len(new_borad)):
        print(f'The board is not squart!')
        return 0
        
    # Making board to 2D array 
    size_borad = len(new_borad)
    size_row = int(math.sqrt(size_borad))
    
    to_d_borad = []
    for i in range(0,size_borad,size_row):
        a = []
        for j in range(i,size_row + i):
            # print(new_borad[j])
            a.append(new_borad[j])
        to_d_borad.append(a)
    
    print(to_d_borad)
    
    for row in range(0,size_row):
        for column in range (0,size_row):
            a = str(to_d_borad[row][column])
            if a == 'P':
                to_d_borad = pawn(to_d_borad , row , column,size_row)
                # display(to_d_borad)
            if a == 'R':
                to_d_borad = rook(to_d_borad , row , column,size_row)
                # display(to_d_borad)
#             if a == 'B':
#             if a == 'Q':
# a
    