import sys
import time
# vars for board
row_one = ["[ ]", "[ ]", "[ ]"]
row_two = ["[ ]", "[ ]", "[ ]"]
row_three = ["[ ]", "[ ]", "[ ]"]
# player one
x = "x"
# player two
o = "o"


def print_exit_macro_x():
    print("||################################||")
    print("||================================||")
    print("||===========X WINS===============||")
    print("||================================||")
    print("||################################||")
    time.sleep(120)


def print_exit_macro_o():
    print("||#################################||")
    print("||=================================||")
    print("||============0 WINS===============||")
    print("||=================================||")
    print("||#################################||")
    time.sleep(120)



# detects winner winner chicken dinner
def check_win():
    # checking player 1 (x)
    # horizontal check
    if row_one == ['[X]', '[X]', '[X]'] or row_two == ['[X]', '[X]', '[X]'] or row_three == ['[X]', '[X]', '[X]']:
        print_exit_macro_x()
    # vertical row check
    if row_one[0] == '[X]' and row_two[0] == '[X]' and row_three[0] == '[X]':
        print_exit_macro_x()
    if row_one[1] == '[X]' and row_two[1] == '[X]' and row_three[1] == '[X]':
        print_exit_macro_x()
    if row_one[2] == '[X]' and row_two[2] == '[X]' and row_three[2] == '[X]':
        print_exit_macro_x()
    # cross row
    if row_one[0] == '[X]' and row_two[1] == '[X]' and row_three[2] == '[X]':
        print_exit_macro_x()
    if row_one[2] == '[X]' and row_two[1] == '[X]' and row_three[0] == '[X]':
        print_exit_macro_x()

    # checking player 2 (o)
    # horizontal check
    if row_one == ['[O]', '[O]', '[O]'] or row_two == ['[O]', '[O]', '[O]'] or row_three == ['[O]', '[O]', '[O]']:
        print_exit_macro_o()
    if row_one[0] == '[O]' and row_two[0] == '[O]' and row_three[0] == '[O]':
        print_exit_macro_o()
    if row_one[1] == '[O]' and row_two[1] == '[O]' and row_three[1] == '[O]':
        print_exit_macro_o()
    if row_one[2] == '[O]' and row_two[2] == '[O]' and row_three[2] == '[O]':
        print_exit_macro_o()
        # cross row
    if row_one[0] == '[O]' and row_two[1] == '[O]' and row_three[2] == '[O]':
        print_exit_macro_o()
    if row_one[2] == '[0]' and row_two[1] == '[0]' and row_three[0] == '[0]':
        print_exit_macro_o()
