import frontend
import rules
from rules import row_one, row_two, row_three

# handles win system && exits program
frontend.intro()
# player one
x = "x"

# player two
o = "o"
rules.check_win()
# shows field and dec vars
frontend.board()

# main loop, handles input, pushes sign in row and field
for x in range(9):
    rules.check_win()
    frontend.x_turn()
    input_row = int(input("type in row [1-3]: "))
    input_field = int(input("type in field [1-3]: "))
    # x' turn
    # handles input for row one
    if input_row == 1 and input_field == 1:
        row_one.pop(0)
        row_one.insert(0, "[X]")
        frontend.board()
    elif input_row == 1 and input_field == 2:
        row_one.pop(1)
        row_one.insert(1, "[X]")
        frontend.board()
    elif input_row == 1 and input_field == 3:
        row_one.pop(2)
        row_one.insert(2, "[X]")
        frontend.board()

    # handles input for row two
    elif input_row == 2 and input_field == 1:
        row_two.pop(0)
        row_two.insert(0, "[X]")
        frontend.board()
    elif input_row == 2 and input_field == 2:
        row_two.pop(1)
        row_two.insert(1, "[X]")
        frontend.board()
    elif input_row == 2 and input_field == 3:
        row_two.pop(2)
        row_two.insert(2, "[X]")
        frontend.board()

    # handles input for row three
    elif input_row == 3 and input_field == 1:
        row_three.pop(0)
        row_three.insert(0, "[X]")
        frontend.board()
    elif input_row == 3 and input_field == 2:
        row_three.pop(1)
        row_three.insert(1, "[X]")
        frontend.board()
    elif input_row == 3 and input_field == 3:
        row_three.pop(2)
        row_three.insert(2, "[X]")
        frontend.board()

    rules.check_win()

    # o's turn

    # handles user input
    input_row = int(input("type in row [1-3]: "))
    input_field = int(input("type in field [1-3]: "))

    if input_row == 1 and input_field == 1:
        row_one.pop(0)
        row_one.insert(0, "[0]")
        frontend.board()
    elif input_row == 1 and input_field == 2:
        row_one.pop(1)
        row_one.insert(1, "[0]")
        frontend.board()
    elif input_row == 1 and input_field == 3:
        row_one.pop(2)
        row_one.insert(2, "[0]")
        frontend.board()

    # handles input for row two
    elif input_row == 2 and input_field == 1:
        row_two.pop(0)
        row_two.insert(0, "[0]")
        frontend.board()
    elif input_row == 2 and input_field == 2:
        row_two.pop(1)
        row_two.insert(1, "[0]")
        frontend.board()
    elif input_row == 2 and input_field == 3:
        row_two.pop(2)
        row_two.insert(2, "[0]")
        frontend.board()

    # handles input for row three
    elif input_row == 3 and input_field == 1:
        row_three.pop(0)
        row_three.insert(0, "[0]")
        frontend.board()
    elif input_row == 3 and input_field == 2:
        row_three.pop(1)
        row_three.insert(1, "[0]")
        frontend.board()
    elif input_row == 3 and input_field == 3:
        row_three.pop(2)
        row_three.insert(2, "[O]")
        frontend.board()
    rules.check_win()
