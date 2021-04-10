




#main method

def main():

    #create a string of text that represents the board
    board = str(input("input the sudoku numbers using 0 as empty (all in one line)"))
    
    #call the sudokuSolver algorithm, which will print out any solutions
    sudokuSolver(board)




#printBoard takes a board and then prints it so that it is formatted in a sudoku
# board manner

def printBoard(board):

    index = 0

    print(".-----------------------.")
    for item in range(len(board)):
        if (item % 3 == 0):
            print("| ",end="")
        if (item % 9 == 0 and item != 0):
            print("\n| ",end="")
        if (item % 27 == 0 and item != 0):
            print("------+-------+------ |\n| ",end="")
        print(board[item],"",end="")
    print("|\n'-----------------------'")





#matrixToIndex takes in the row and column, and then takes that and turns it 
# into an index value in a linear array. It is assumed that the matrix 
# dimensions are 9 X 9. 

def matrixToIndex(row,column):

    #the index value is equal to the column number added to the row number times 9
    return (row * 9) + column





#indexToMatrix - this function takes in an index and returns one of the components
# of the matrix that that index value represents. The x or y component returned
# is given by the corresponding funciton indexToMatrixX or indexToMatrixY

def indexToMatrixX(index):
    return index % 9
    




def indexToMatrixY(index):
    return index // 9





#sudokusolver algorithm expects to find a continuous string for the board
# that uses 0 to represent blanks in the sudoku board

def sudokuSolver(board):

    #base case is if the board is full
    if ( isFull(board) ):
        # if the board is solved then we print the solution to the screen        
        if ( isSolved(board) ):
            printBoard(board)
        
        return

    #if not full insert a number into the board and recurse
    else:

        #we will insert the numbers 1 through 9 into the board and call
        # the sudoku solving algorithm on the new board that contains the 
        # inserted number
        for i in range(9):
            if validInsert(i+1,board):
                sudokuSolver( newBoard(i+1,board) )

        return





#isFull algorithm takes in a board and iterates through the string of text
# named board and will look for any 0s. If no 0s are found then it means that
# the board is full. If the board is full return True and if board is not full 
# return False

def isFull(board):

    #we create a variable called full to act as a flag to tell us if the board
    # is full or not. We will assume it is full for now
    full = True

    #we will iterate through the string of text to look for the number 0
    for i in range(len(board)):

        # if we find the number 0 then we set the full variable to false
        if (board[i] == "0"):
            full = False
            return full

    #return whether the puzzle is full or not    
    return full





#isSolved takes in a board and then it goes through and checks to see if the
# board is solved or an invalid solution. If the solution is invalid it will
# return False, and if the solution is valid it will return the value of True

def isSolved(board):
    
    #make a list to hold found values to check for duplicates
    # and make a variable called solved to determine if the board is solved or
    # not. We will assume that it is solved unless proved otherwise
    numberList = ["0","0","0","0","0","0","0","0","0"]
    solved = True

    #check vertical:

    #we iterate through all the column items in each row
    for row in range(9):
        #reset the number list
        numberList = ["0","0","0","0","0","0","0","0","0"]

        for column in range(9):
            
            #if the value in numberList at the index equal to the specified
            # value in board is equal to 0 then
            # this is the first time this number has been seen in this row
            if numberList[ int(board[ matrixToIndex(row,column) ]) -1 ] == "0":
                #set the number in number list to one to mark that we have been
                # here already
                numberList[ int(board[ matrixToIndex(row,column) ]) -1 ] = "1"
            # if the number is not zero then we have a duplicate number
            else:
                #if we have a duplicate then we set solve to false
                solved = False
                return solved

    #check horizontal:

    #we iterate through all the row items in each column
    for column in range(9):
        #reset the number list
        numberList = ["0","0","0","0","0","0","0","0","0"]

        for row in range(9):
            
            #if the value in numberList at the index equal to the specified
            # value in board is equal to 0 then
            # this is the first time this number has been seen in this column
            if numberList[ int(board[ matrixToIndex(row,column) ]) -1 ] == "0":
                #set the number in number list to one to mark that we have been
                # here already
                numberList[ int(board[ matrixToIndex(row,column) ]) -1 ] = "1"
            
            #if the number is not zero then we have a duplicate number
            else:
                #if we have a duplicate then we set solve to False
                solved = False
                return solved

    #check boxes:

    #generate the index of the top left corner of each mini-box
    for miniRow in range(3):
        for miniColumn in range(3):
            
            #reset the numberList
            numberList = ["0","0","0","0","0","0","0","0","0"]

            #iterate through a small 3X3 square
            for row in range(3):
                for column in range(3):

                    #if the nember in numberList at the index equal to the number in
                    # the spot of the board that we are looking at is equal to 0 then
                    # this is the first time that this number has been seen
                    if numberList [ int(board[matrixToIndex(miniRow * 3 + row, miniColumn * 3 + column) ]) -1 ] == "0":
                        #set the number in the numberList to 1 to mark that we have been
                        # here already
                        numberList[ int(board[ matrixToIndex(miniRow * 3 + row, miniColumn * 3 + column) ]) -1 ] = "1"
                    
                    #if the number is not zero then we have a duplicate number
                    else:
                        #if we have a duplicte then we set solve to False
                        solved = False
                        return solved

    return solved





#newBoard algorithm will look at the string of text called board, and then where
# it finds the first 0 we will put in the value provided for i instead, after which
# we will continue to put in the remaining characters in the original string of 
# text to create a new one called "newBoard" that is then returned.

def newBoard(i,board):

    #create a variable called newBoard, and set it to an empty string of text
    # then create a variable called inserted, which keeps track of whether or
    # not we have already put in our new value
    newBoard = ""
    inserted = False

    #we loop through the string of text in the provided board
    for j in range(len(board)):

        #when we reach an empty space
        if (board[j] == "0"):

            #and we have not already put in our new value, then we put in the
            # value i instead of 0, and then mark that we have inserted something
            # that way we don't do it again if we reach another empty space
            if (not inserted):
                newBoard += str(i)
                inserted = True

            #if the space is empty and we have already inserted the new value,
            # then we procede with putting in the 0
            else:
                newBoard += board[j]

        #if the space already has a number then we just add that to the new string
        else:        
            newBoard += board[j]

    #after transcribing the values of the old string with the new value added in
    # we return the new updated string
    return newBoard





#validInsert - takes in a number and a board, and then it looks for the first
# blank space in the board. Then it checks if the number would be a valid move
# if put into that spot. If the move is valid the function returns True, and if
# it is not then the function returns false

def validInsert(i,board):

    #create a variable to hold the index in board that the empty space to be filled
    # is located
    index = 0

    #find the index of the first available empty space
    while board[index] != "0":
        index = index + 1

    #save the location in matrix form to the variables spaceX and spaceY
    spaceColumn = indexToMatrixX(index)
    spaceRow = indexToMatrixY(index)

    
    
    #Check horizontal
    
    #we iterate through the row that the number to be inserted is located in, and 
    # if that number already exists in the row, then the number is invalid
    for j in range(9):
        if ( board[ matrixToIndex(spaceRow,j) ] == str(i) ):
            return False

    #check vertical

    #we iterate through the column that the number to be insrted is located in, and 
    # if that number alread exists in the column, then the number is invalid
    for j in range(9):
        if (board[ matrixToIndex(j,spaceColumn) ] == str(i) ):
            return False

    #check miniBox

    #we look at the column and the row to determine which mini-box the blank space is in
    # and we identify the top left corner of the mini-box
    miniColumn = spaceColumn // 3 
    miniRow = spaceRow // 3
    
    #we iterate through the mini-box
    for row in range(3):
        for column in range(3):

            #if we find the number to be inserted in the minibox then the number to be inserted
            # is invalid
            if (board[ matrixToIndex(miniRow * 3 + row, miniColumn * 3 + column) ] == str(i) ):
                return False
    return True





################################################################################






# run the main funciton

main()





