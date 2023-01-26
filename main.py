import random
import os





def get_numbers():
    first_number = random.randint(1,20)
    second_number = random.randint(1,20)
    return first_number, second_number

def get_operation():
    operation_list = ["-", "+"]
    return random.choice(operation_list)

def ask_question():
    result = 0
    answer = 0
    number_1, number_2 = get_numbers()
    while number_1 < number_2:
        number_1, number_2 = get_numbers()
    if get_operation() == "-":
        result = number_1 - number_2
        answer = int(input(f"{number_1} - {number_2} = "))
    elif get_operation() == "+":
        result = number_1 + number_2
        answer = int(input(f"{number_1} + {number_2} = "))
    check_answer(answer, result)

    
def check_answer(answer, result):
    if answer == result:
        print("giusto")
    else:
        print("sbagliato")







ask_question()


