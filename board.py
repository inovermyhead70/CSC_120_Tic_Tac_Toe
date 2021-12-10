board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
         
currentPlayer = "X"
gameContinue = True  
winner = None       
         
def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
   

    
def player_input(board):
    global currentPlayer
    
    print("It is your turn " + currentPlayer)
    position = int(input("Enter a number 1-9: "))
    
    if position >= 1 and position <= 9 and board[position-1] == "-":
        board[position-1] = currentPlayer
    else:
        print("Number invalid or position taken!")    
        
      
def check_row(board):
    global winner  
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True  
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True        

def check_column(board):
    global winner  
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True  
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def check_diag(board):
    global winner  
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[6] == board[4] == board[2] and board[6] != "-":
        winner = board[6]
        return True

def check_win():
    if check_row(board) or check_column(board) or check_diag(board):
        print(f"The winner is {winner}")
        gameContinue = False

def check_tie(board):
    global gameContinue
    if "-" not in board:
        print_board(board)
        print("it is a tie!")
        gameContinue = False

      
def switch_player():
    global currentPlayer
    if currentPlayer == "X":
      currentPlayer = "O"
    else:
      currentPlayer = "X"
       
while gameContinue:
  print_board()
  player_input(board)
  check_win()
  check_tie(board)
  switch_player()
  