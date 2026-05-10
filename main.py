# 01-python_basics__workshop__task03_number-guessing-game-2
#
# import sys
# library for workshops' tasks
from lib.workshop import *
#
from random import randint
#
# constants
ENTER_NUMBER_LIMIT_LOWER=1
ENTER_NUMBER_LIMIT_UPPER=10
#
def get_number(enter_number_limit_lower: int,enter_number_limit_upper: int,msg: str) -> int:
    while True:
        entered_number = int(input(f"{msg}"))
        if entered_number.lower() == "q":
            break
        try:
            entered_number = int(entered_number)
            break
        except ValueError:
            print("... it's not a number!")
    return entered_number

def enter_number (enter_number_limit_lower: int,enter_number_limit_upper: int, msg: str) -> int:
    while True:
        # entered_number = get_number(enter_number_limit_lower,enter_number_limit_upper,msg)
        entered_number = input(f"{msg}")
        if entered_number == "":
            entered_number = 0
            break
        if entered_number.lower() == "x":
            entered_number=-9
            break
        try:
            entered_number = int(entered_number)

            if entered_number>enter_number_limit_upper:
                print(f" ... the number is greater than the limit {enter_number_limit_upper}!")
            elif entered_number<enter_number_limit_lower:
                print(f" ... the number is less than the limit {enter_number_limit_lower}!")
            else:
                break
        except ValueError:
            print("... it's not a number!")

    return entered_number

def get_answer(msg: str) -> str:
    answer_list = []
    while True:
        try:
            answer = str(input(f"{msg}"))
            answer = answer+"========".lower()
            answer_list=[answer[4],answer[0]]
            if "q" in answer_list:
                answer="q"
                break
            elif "h" in answer_list:
                answer = "h"
                break
            elif "l" in answer_list:
                answer = "l"
                break
            elif "x" in answer_list:
                answer = "x"
                break
            else:
                # print("... it's not correct answer! Use keys: l,h,q (or x to exit) ")
                print(f"Don't cheat ! Use keys: l,h,q (or x to exit)")
        except ValueError:
            print("... it's not a string!")
    return answer


workshop_task_header()
# main - start
print(f"Think about a number from {ENTER_NUMBER_LIMIT_LOWER} to {ENTER_NUMBER_LIMIT_UPPER} and let me guess it!")
bet_number = enter_number(ENTER_NUMBER_LIMIT_LOWER,ENTER_NUMBER_LIMIT_UPPER," - You can note that number (or press \"x\" to exit): ")
if (bet_number == -9):
     sys_exit()
if (bet_number > 0):
    print(f" - Thanks, I noted the number {bet_number}.")
print(60 * "-")

i=0
guess_min=ENTER_NUMBER_LIMIT_LOWER
guess_max=ENTER_NUMBER_LIMIT_UPPER
while True:
    i += 1
    if (i>30):
        sys_exit(f"\n The number of iterations has reached {str(i)}, no fun, I'm done !")
        break

    guess=int((guess_max-guess_min)/2 + guess_min)
    answer = get_answer(f"#"+str(i).zfill(2)+" - Guessing: "+str(guess)+" - this number is: too [l]ow | too [h]ight | you [q]uessed: ")

    if answer=="x":
        sys_exit()
    elif answer=="q":
        if (bet_number>0):
            if bet_number==guess:
                print(f"\n I won !")
                break
            else:
                print(f"\n You marked as a guess number {guess} but you note the number {bet_number}!")
                break
        else:
            print(f"\n I won !")
            break
    elif answer == "h":
        guess_max=guess
    elif answer == "l":
        guess_min=guess
    else:
        print(f"Don't cheat !")

# main - end
workshop_task_footer()
