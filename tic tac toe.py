board = [" " for _ in range(9)]
player = "X"
winner = None
game_running = True
print("Tic Tac Toe")
print("-------------")
print(" 0 | 1 | 2 ")
print("-----------")
print(" 3 | 4 | 5 ")
print("-----------")
print(" 6 | 7 | 8 ")
print("-------------")
while game_running:
    print("\nCurrent board:")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

    move = int(input(f"\nPlayer {player}, enter a position (0-8): "))
    if board[move] == " ":
        board[move] = player
    else:
        print("Spot already taken! Try again.")
        continue
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            winner = board[i]
            game_running = False
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            winner = board[i]
            game_running = False
    if board[0] == board[4] == board[8] != " ":
        winner = board[0]
        game_running = False
    if board[2] == board[4] == board[6] != " ":
        winner = board[2]
        game_running = False

    # Check for tie
    if " " not in board and winner is None:
        game_running = False

    # Switch player
    if player == "X":
        player = "O"
    else:
        player = "X"

# Final board and result
print("\nFinal board:")
print(board[0] + " | " + board[1] + " | " + board[2])
print("--+---+--")
print(board[3] + " | " + board[4] + " | " + board[5])
print("--+---+--")
print(board[6] + " | " + board[7] + " | " + board[8])

if winner:
    print(f"\nPlayer {winner} wins!")
else:
    print("\nIt's a tie!")
