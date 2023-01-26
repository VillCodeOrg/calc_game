import random
import os





def get_numbers():
    first_number = random.randint(1,20)
    second_number = random.randint(1,20)
    return first_number, second_number

def get_operation():
    operation_list = "-"
    return random.choice(operation_list)

def check_operation():
    if operation == "-":
        meno(number_1, number_2, answer)

def check_answer(result, answer):
    if result == answer:
        massege = "giusto"
    else:
        massege = "sbagliato"


def question():
    answer = input(f"{number_1} - {number_2} = ")
    check_operation()

def meno(number_1, number_2, answer):
    result = number_1 - number_2
    check_answer(result, answer)




operation = get_operation()
number_1 = get_numbers()[0]
number_2 = get_numbers()[1]
while number_1 <= number_2:
    number_1 = get_operation[0]
    number_2 = get_operation[1]
answer = question()



        



