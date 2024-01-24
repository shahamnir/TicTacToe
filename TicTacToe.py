def row_winner(board):
    #check if there's a row of same symbol and returns its symbol
    if board[1] == board[3] and board[1] == board[5]:# could write board[3] == board[1] == board[5]
        return board[1]
    elif board[8] == board[10] and board[8] == board[12]:
        return board[8]
    elif board[15] == board[17] and board[15] == board[19]:
        return board[15]


def column_winner(board):
    # check if there's a column of same symbol and returns its symbol
    if board[1] == board[8] and board[1] == board[15]:
        return board[1]
    elif board[3] == board[10] and board[3] == board[17]:
        return board[3]
    elif board[5] == board[12] and board[5] == board[19]:
        return board[5]


def diagonal_winner(board):
    # check if there's a diagonal of same symbol and returns its symbol
    if board[1] == board[10] and board[1] == board[19]:
        return board[1]

    elif board[5] == board[10] and board[5] == board[15]:
        return board[5]


def check_winner():
    #check which kind of winner and returns a claim for the winner
    if row_winner(board):
        print(str(row_winner(board)) + " is the winner!")
        return True
    elif column_winner(board):
        print(str(column_winner(board)) + " is the winner!")
        return True
    elif diagonal_winner(board):
        print(str(diagonal_winner(board)) + " is the winner!")
        return True


def validate_action(action):
    if (action == "1" or action == "2" or action == "3"
            or action == "4" or action == "5" or action == "6"
            or action == "7" or action == "8" or action == "9"):
        return True


def action_for_o():
    # placing an o symbol according to the action given
    while not check_winner():
        action = input("Player o  place your mark")
        if not validate_action(action):
            print("wrong placement, try again")
        if action == "7":
            if board[1] == "7":
                board[1] = "o"
                break
            else:
                print("this place is taken, try again")
        elif action == "8":
            if board[3] == "8":
                board[3] = "o"
                break
            else:
                print("this place is taken, try again")
        elif action == "9":
            if board[5] == "9":
                board[5] = "o"
                break
            else:
                print("this place is taken, try again")
        elif action == "4":
            if board[8] == "4":
                board[8] = "o"
                break
            else:
                print("this place is taken, try again")
        elif action == "5":
            if board[10] == "5":
                board[10] = "o"
                break
            else:
                print("this place is taken, try again")
        elif action == "6":
            if board[12] == "6":
                board[12] = "o"
                break
            else:
                print("this place is taken, try again")
        elif action == "1":
            if board[15] == "1":
                board[15] = "o"
                break
            else:
                print("this place is taken, try again")
        elif action == "2":
            if board[17] == "2":
                board[17] = "o"
                break
            else:
                print("this place is taken, try again")
        elif action == "3":
            if board[19] == "3":
                board[19] = "o"
                break
            else:
                print("this place is taken, try again")


    new_board = "".join(board)
    print(new_board)


def action_for_x():
    # placing an x symbol according to the action given
    while not check_winner():
        action = input("Player *  place your mark")
        if not validate_action(action):
            print("wrong placement, try again")
        if action == "7":
            if board[1] == "7":
                board[1] = "*"
                break
            else:
                print("this place is taken, try again")
        elif action == "8":
            if board[3] == "8":
                board[3] = "*"
                break
            else:
                print("this place is taken, try again")
        elif action == "9":
            if board[5] == "9":
                board[5] = "*"
                break
            else:
                print("this place is taken, try again")
        elif action == "4":
            if board[8] == "4":
                board[8] = "*"
                break
            else:
                print("this place is taken, try again")
        elif action == "5":
            if board[10] == "5":
                board[10] = "*"
                break
            else:
                print("this place is taken, try again")
        elif action == "6":
            if board[12] == "6":
                board[12] = "*"
                break
            else:
                print("this place is taken, try again")
        elif action == "1":
            if board[15] == "1":
                board[15] = "*"
                break
            else:
                print("this place is taken, try again")
        elif action == "2":
            if board[17] == "2":
                board[17] = "*"
                break
            else:
                print("this place is taken, try again")
        elif action == "3":
            if board[19] == "3":
                board[19] = "*"
                break
            else:
                print("this place is taken, try again")

    new_board = "".join(board)
    print(new_board)


def player_turns():
    # managing the turns of the players
    for i in range(10):
        if check_winner():
            break
        if i == 9 and not check_winner():
            print("it's a tie!")
            break
        elif i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            action_for_x()
        elif i == 1 or i == 3 or i == 5 or i == 7:
            action_for_o()


print("Tic Tac Toe")
board = ["|", "7", "|", "8", "|", "9", "\n", "|", "4", "|", "5", "|", "6", "\n", "|", "1", "|", "2", "|", "3"]
new_board = "".join(board)
print(new_board)
player_turns()
