
#!/usr/bin/python3
"""
^
shebang line [You can change it or remove it as per you need]
"""


import random
#bot = random.randint(0, 8)
"""
Createing a game board  and displaying it using list
"""
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
looper = True


def show():
    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("{} | {} | {}".format(board[6], board[7], board[8]))


show()

"""
function for check each possible lines
"""


def check_line(char, spot1, spot2, spot3):
    if(board[spot1] == char and board[spot2] == char and board[spot3] == char):
        return True
    else:
        return False


"""
this function checks each possible combination for victory and return the result
"""


def check_all(char):
    """
    row combinations
    """
    if check_line(char, 0, 1, 2):
        #print("{} is winner".format(char))
        return True
    if check_line(char, 3, 4, 5):
        #print("{} is winner".format(char))
        return True
    if check_line(char, 6, 7, 8):
        #print("{} is winner".format(char))
        return True

    """
    column combinations
    """
    if check_line(char, 0, 3, 6):
        #print("{} is winner".format(char))
        return True
    if check_line(char, 1, 4, 7):
        #print("{} is winner".format(char))
        return True
    if check_line(char, 2, 5, 8):
        #print("{} is winner".format(char))
        return True

    """
    cross combinations
    """
    if check_line(char, 0, 4, 8):
        #print("{} is winner".format(char))
        return True
    if check_line(char, 2, 4, 6):
        #print("{} is winner".format(char))
        return True


"""
main loop whin runs until the player or bot wins
"""
while looper:

    u_input = int(input("Select The number according u want to place X : "))

    if board[u_input] != 'x' and board[u_input] != 'o':
        board[u_input] = 'x'

        # check
        if check_all('x') == True:
            print("x wins")
            print("__________________")
            print(show())

            break

        """
        In following loop we are generating input for bot from random function
        though it may possible that random function may generate same number it has generated already
        so we break the loop in that situation and regenerate the number and keep finding the spot.
        """
        while True:
            bot = random.randint(0, 8)
            """
            in following condition i am checking whether the spot is takrn by bot or even user
            if that user part removed it may possible that the spot is takrn by player[X] replaced by bot[O]
            """
            if board[bot] != 'o' and board[bot] != 'x':
                board[bot] = 'o'

            # check
                if check_all('o') == True:
                    print("bot wins")
                    print("__________________")
                    looper = False
                    show()
                    print("__________________")
                    break

                break
    else:
        print("This spot is already taken!!!")
        break
    show()
