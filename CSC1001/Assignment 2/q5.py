# Question 6: Eight Queens with Blocked Squares
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary
from numpy.ma.extras import row_stack


def allowPlace(pos, row, col):
    blocked = [(0,0), (1,3), (7,5)]
    if (row, col) in blocked:
        return False

    for r in range(row):
        c = pos[r]
        if c == col or abs(c-col) == abs(r-row): #diagonal and on the same column check
            return False
    return True


def solution(board, pos, row):
    if row == 8:
        for r in range(8): #make the board
            for c in range(8):
                if pos[r] == c:
                    board[r][c] = "|Q"
        stringify_board = "\n".join(["".join(x + ["|"]) for x in board])  # change it to string so it can be printed
        print(stringify_board, end="\n\n")

        for r in range(8): #undo the board (fresh)
            for c in range(8):
                board[r][c] = "| "
        return False

    for col in range(8):
        if allowPlace(pos, row, col):
            pos[row] = col
            solution(board, pos, row+1)
            pos[row] = -1
    return False


def eight_queens_blocked_squares():
    ''' 
    By calling this function, it will display one solution of the Eight Queens
    parameter: no
    return: no
    '''
    # NOTE: you CANNOT just pre-define a solution and display it.
    # Please use algorithm to display a possible solution
    # ------- Your code start here -------
    board = [["| " for x in range(8)] for y in range(8)] #create the board
    solution(board, [-1]*8, 0)
    # ------- End of your code -----------


# Call the function to print the solution
if __name__ == '__main__':
    eight_queens_blocked_squares()