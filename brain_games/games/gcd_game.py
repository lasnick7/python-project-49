import random
from ..cli import game
from ..utils import find_gcd


def generate_question_for_gcd_game():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    problem_string = f"{a} {b}"
    correct_answer = find_gcd(a, b)
    return problem_string, str(correct_answer)


game_description = "Find the greatest common divisor of given numbers."


def gcd_game():
    return game(game_description, generate_question_for_gcd_game)