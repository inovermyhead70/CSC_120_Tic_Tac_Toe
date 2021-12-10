board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
         
currentPlayer = "X"
gameContinue = True         
         
def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
   
    
def check_mark(board):
    global currentPlayer
    print("It is your turn " + currentPlayer) 
    choice = int(input("Enter a number 1-9: "))
    if choice >= 1 and choice <= 9 and board[choice-1] == "-":
      board[choice-1] = currentPlayer
    else:
      print("Spot taken. Please choose again!")
      
def switch_player():
    global currentPlayer
    if currentPlayer == "X":
      currentPlayer = "O"
    else:
      currentPlayer = "X"
       
while gameContinue:
  print_board()
  check_mark(board)
  switch_player()
  