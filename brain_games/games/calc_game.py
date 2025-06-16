import random
import operator
from ..cli import game


def generate_question_for_calc_game():
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)

    operators = ['*', '-', '+']
    operations = {
        "*": operator.mul,
        "+": operator.add,
        "-": operator.sub,
    }
    o = random.choice(operators)

    problem_string = f"{operand1} {o} {operand2}"
    correct_answer = operations[o](operand1, operand2)
    return problem_string, str(correct_answer)


game_description = "What is the result of the expression?"


def calc_game():
    return game(game_description, generate_question_for_calc_game)
