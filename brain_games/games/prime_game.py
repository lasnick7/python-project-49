import random
from ..cli import game
from ..utils import is_prime


def generate_question_for_prime_game():
    x = random.randint(1, 100)
    is_x_prime = is_prime(x)

    problem_string = str(x)
    correct_answer = "yes" if is_x_prime else "no"

    return problem_string, correct_answer


game_description = """Answer "yes" if given number is prime. Otherwise answer "no"."""  # noqa: E501


def prime_game():
    return game(game_description, generate_question_for_prime_game)
