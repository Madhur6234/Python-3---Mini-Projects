import random

#To Display Board
def display_board(board):
    print('   |     |   \n' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] + '  \n   |     | \n-------------')
    print('   |     |   \n' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] + '  \n   |     | \n-------------')
    print('   |     |   \n' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] + '  \n   |     | ')

#Choose Any Player
def choose_first():
    if random.randint(0,1)==0:
        return 'Player 1'
    else:
        return 'Player 2'

#To Take Input
def player_input():
    marker =''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, Choose 'X' or 'O': ").upper()

    palyer1 = marker

    if palyer1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return (palyer1, player2)

#Place Marker
def place_marker(board, marker, position):
    board[position] = marker

#To Check Winner
def win_check(board, mark):
    return(board[1]==board[2]==board[3]==mark or
           board[4]==board[5]==board[6]==mark or
           board[7]==board[8]==board[9]==mark or
           board[1]==board[4]==board[7]==mark or
           board[2]==board[5]==board[8]==mark or
           board[3]==board[6]==board[9]==mark or
           board[1]==board[5]==board[9]==mark or
           board[3]==board[5]==board[7]==mark)

#Check Space Occupied or Not
def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False

#To Check Board is Full or Not
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#Select Position
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a Position: (1-9)'))
    return position

#Play Again or Not
def replay():
    choice = input("Play Again? Enter 'Y' or 'N': ").upper()
    return choice == 'Y'

#Real Game
while True:
    print('Welcome to Tic Tac Toe')

    #SET EVERYTHING UP(like Board, Who Goes First, Choose Marker)
    theBoard = [' ']*10

    player1_marker , player2_marker = player_input()

    turn = choose_first()
    print(turn + ', Will Go First')

    play_game = input('Ready To Play? Y or N? ').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    #Gameplay
    while game_on:

        if turn == 'Player 1':
            #Display Board
            display_board(theBoard)

            #Select Position
            print('Player 1:')
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            #Win Check
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Player 1 Has Won The Game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('TIE!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            # Display Board
            display_board(theBoard)

            # Select Position
            print('Player 2:')
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            # Win Check
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 Has Won The Game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('TIE!')
                    game_on = False
                else:
                    turn = 'Player 1'

    #For Replay or Not
    if not replay():
        break
