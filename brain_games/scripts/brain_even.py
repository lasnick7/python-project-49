import prompt
import random
from ..cli import welcome_user


def is_even(n):
    return 'yes' if n % 2 == 0 else 'no'


def even_game(name):
    game_description = """Answer "yes" if the number is even, otherwise answer "no"."""
    print(game_description)

    errors = 0
    score = 0
    while score < 3 and errors == 0:
        random_integer = random.randint(1, 1000)
        correct_answer = is_even(random_integer)
        question = f"Question: {random_integer}"
        print(question)
        player_answer = prompt.string("Your answer: ")
        if correct_answer == player_answer:
            score += 1
            print("Correct!")
        else:
            errors += 1
            break

    if score < 3:
        print(f"""'{player_answer} is wrong answer ;(. Correct answer was '{correct_answer}'.'""")
        print(f"Let's try again, {name}!")
    else:
        print(f"Congratulations, {name}!")



def main():
    name = welcome_user()
    even_game(name)

if __name__ == '__main__':
    main()
