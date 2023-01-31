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
    is_correct = False
    result = 0
    answer = 0
    number_1, number_2 = get_numbers()
    while number_1 < number_2:
        number_1, number_2 = get_numbers()
    operation = get_operation()
    while not is_correct:
        if operation == "-":
            result = number_1 - number_2
            answer = input(f"{number_1} - {number_2} = ")
            is_correct = check_answer(answer, result)
        elif operation == "+":
            result = number_1 + number_2
            answer = input(f"{number_1} + {number_2} = ")
            is_correct = check_answer(answer, result)

    
def check_answer(answer, result):
    os.system('cls')
    if answer == "q":
        exit(0)
    elif int(answer) == result:
        print("giusto")
        return True   
    else:
        print("sbagliato")
        return False





os.system('cls')
while 0 == 0:
    ask_question()


