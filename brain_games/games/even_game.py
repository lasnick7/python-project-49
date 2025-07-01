import random
from ..utils import is_even
from ..cli import game


def generate_question_for_even_game():
    random_integer = random.randint(1, 1000)
    correct_answer = is_even(random_integer)
    return random_integer, correct_answer


game_description = """Answer "yes" if the number is even, otherwise answer "no"."""  # noqa: E501


def even_game():
    return game(game_description, generate_question_for_even_game)

