import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def game(game_description, question_func):
    print(game_description)

    score = 0
    player_correct_answers = [True, '', '']
    while score < 3:
        question_data, correct_answer = question_func()
        question = f"Question: {question_data}"
        print(question)
        player_answer = prompt.string("Your answer: ")
        if correct_answer == player_answer:
            score += 1
            print("Correct!")
        else:
            player_correct_answers[0] = False
            player_correct_answers[1] = player_answer
            player_correct_answers[2] = correct_answer
            return player_correct_answers
    return player_correct_answers


def end_of_the_game(name, win, player_answer, correct_answer):
    if win:
        print(f"Congratulations, {name}!")
    else:
        print(f"""'{player_answer} is wrong answer ;(. Correct answer was '{correct_answer}'.'""")  # noqa: E702,E203,E231
        print(f"Let's try again, {name}!")
