game = [[" " for i in range(3)] for j in range(3)]


def print_board():

    print(f"""
     --- --- ---
    | {game[0][0]} | {game[0][1]} | {game[0][2]} |
     --- --- ---
    | {game[1][0]} | {game[1][1]} | {game[1][2]} |
     --- --- ---
    | {game[2][0]} | {game[2][1]} | {game[2][2]} |
     --- --- ---
    """)


def player_move(pn):

    if pn == 1:
        symbol = "O"
    else:
        symbol = "X"

    move = input(f"Player no.{pn}, enter the coordinates (row number, column number) for '{symbol}': ")
    move = move.split(",")

    mr = int(move[0]) - 1
    mc = int(move[1]) - 1

    if game[mr][mc] == " ":
        game[mr][mc] = symbol
        print_board()
    else:
        print("Incorrect coordinates or the position is taken.")
        player_move(pn)


def checking_winner():

    for i in range(0, 3):
        if game[i][0] == game[i][1] == game[i][2]:  # checking row winner
            if game[i][0] == "O":
                return 1
            elif game[i][0] == "X":
                return 2

        elif game[0][i] == game[1][i] == game[2][i]:  # checking column winner
            if game[0][i] == "O":
                return 1
            elif game[0][i] == "X":
                return 2

    if game[0][0] == game[1][1] == game[2][2]:  # checking I diagonal winner
        if game[0][0] == "O":
            return 1
        elif game[0][0] == "X":
            return 2

    elif game[2][0] == game[1][1] == game[0][2]:  # checking II diagonal winner
        if game[2][0] == "0":
            return 1
        elif game[2][0] == "X":
            return 2


print("Welcome to the tic-tac-toe game!")
print_board()

player_move(pn=1)
r = 0
while r < 4:
    player_move(pn=2)
    player_move(pn=1)
    if r >= 1:          # There is no point in checking winner until at least one player has made three moves
        if checking_winner() == 1:
            print("End of the game!\nPlayer number 1 is the winner!")
            break
        elif checking_winner() == 2:
            print("End of the game!\nPlayer number 1 is the winner!")
            break
    if r == 3:          # There is no winner and the moves are over
        print("End of the game!\nDraw!")
    r += 1


