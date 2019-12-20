board = [
    [7,8,0,4,0,0,1,2,0],
    [5,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Function to pick empty square
# Can just loop through, and try all numbers
# Function to find if num is valid
def display_board(given):

    for i in range(len(given)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(given[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                
            if j == 8:
                print(given[i][j])
            else:
                print(str(given[i][j]) + " ", end="")


# Find an empty square, which returns the position

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col


# Check if the board is valid
def is_valid(board, num, pos):

    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

#display_board(board)
