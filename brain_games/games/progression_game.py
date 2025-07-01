import random
from ..cli import game


def generate_question_for_progression_game():
    dummy = ".."
    step = random.randint(1, 25)
    hidden_index = random.randint(0, 9)

    correct_answer = 0
    start = random.randint(1, 100)
    progression = []
    for i in range(10):
        curr = start + i * step
        if i == hidden_index:
            correct_answer = str(curr)
            progression.append(dummy)
        else:
            progression.append(str(curr))

    problem_string = " ".join(progression)

    return problem_string, correct_answer


game_description = "What number is missing in the progression?"


def progression_game():
    return game(game_description, generate_question_for_progression_game)
