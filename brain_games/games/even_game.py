import random
from ..utils import is_even
from ..cli import game


def generate_question_for_even_game():
    random_integer = random.randint(1, 1000)
    correct_answer = is_even(random_integer)
    return random_integer, correct_answer


game_description = """Answer "yes" if the number is even, otherwise answer "no"."""


def even_game():
    return game(game_description, generate_question_for_even_game)

# def even_game():
#     game_description = """Answer "yes" if the number is even, otherwise answer "no"."""
#     print(game_description)
#
#     score = 0
#     player_correct_answers = [True, '', '']
#     while score < 3:
#         random_integer = random.randint(1, 1000)
#         correct_answer = is_even(random_integer)
#         question = f"Question: {random_integer}"
#         print(question)
#         player_answer = prompt.string("Your answer: ")
#         if correct_answer == player_answer:
#             score += 1
#             print("Correct!")
#         else:
#             player_correct_answers[0] = False
#             player_correct_answers[1] = player_answer
#             player_correct_answers[2] = correct_answer
#             return player_correct_answers
#     return player_correct_answers
