theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ',
            'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'
count=0;
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
   # theBoard[move] = turn
    if theBoard[move] == ' ':
        theBoard[move] = turn
        count += 1
    else:
        print("That place is already filled.\nMove to which place?")
        continue
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)

def winner():
    if count>=5:
     if theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] != ' ':  # across the top
        printBoard(theBoard)
        print("\nGame Over.\n")
        print(" **** " + turn + " won. ****")


     elif theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] != ' ':  # across the middle
        printBoard(theBoard)
        print("\nGame Over.\n")
        print(" **** " + turn + " won. ****")



