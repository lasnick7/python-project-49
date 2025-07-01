from ..cli import welcome_user, end_of_the_game
from ..games.progression_game import progression_game


def main():
    name = welcome_user()
    game_result = progression_game()
    end_of_the_game(name, *game_result)


if __name__ == '__main__':
    main()
