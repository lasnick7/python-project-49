from ..cli import welcome_user, end_of_the_game
from ..games.calc_game import calc_game


def main():
    name = welcome_user()
    game_result = calc_game()
    end_of_the_game(name, *game_result)


if __name__ == '__main__':
    main()
