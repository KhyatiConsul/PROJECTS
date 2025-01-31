def player_input(player1):
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return player2

def display_board(board):
  print (board[9] + ' |' + board[8] + '|' + board[7])
  print ('--|-|--')
  print (board[6] + ' |' + board[5] + '|' + board[4])
  print ('--|-|--')
  print (board[3] + ' |' + board[2] + '|' + board[1])

def win_check(board, mark):
  return ((board[7] == mark and board[8] == mark and board[9] == mark) or
          (board[4] == mark and board[5] == mark and board[6] == mark) or
          (board[1] == mark and board[2] == mark and board[3] == mark) or
          (board[7] == mark and board[4] == mark and board[1] == mark) or
          (board[8] == mark and board[5] == mark and board[2] == mark) or
          (board[9] == mark and board[6] == mark and board[3] == mark) or
          (board[7] == mark and board[5] == mark and board[3] == mark) or
          (board[9] == mark and board[5] == mark and board[1] == mark))

def full_board_check(board):
    for i in range (1,10):
        if board[i] == ' ':
            return False
    return True

def place_marker(board, marker, position):
    board[position] = marker

def player_choice(board):
    position = 0
    while position not in range (1,10) or board[position] != ' ':
        position =  int (input ("enter the next position (1-9): "))
    return position

def replay():
    return input("do u want to play once again? (y/n): ").lower() == 'y'

print ("let's play tic-tac-toe!")
print ("board setup is like this-")
print ('9' + ' |' + '8' + '|' + '7')
print ('--|-|--')
print ('6' + ' |' + '5' + '|' + '4')
print ('--|-|--')
print ('3' + ' |' + '2' + '|' + '1')

game_play =  input("do u wish to continue? (y/n): ").lower()
if game_play == 'y':
    game_on = True
else:
    print("Goodbye!")
    game_on = False

while game_on == True:
    theBoard = [' ']*10
    player1 = input("do u want to be x or o?: ").upper()
    player2_marker = player_input(player1)
    player2 = player2_marker
    turn = player1
    print ( turn + ' will go first')

    while game_on:
        if turn == player1:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1, position)

            if win_check(theBoard, player1):
                display_board(theBoard)
                print ("player1 won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print ("the game is a draw!")
                    break
                else:
                    turn = player2
                
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2, position)
            if win_check(theBoard, player2):
                display_board(theBoard)
                print ("Player2 won the game!")
                game_on = False
            else:
                turn = player1

    if not replay():
        break