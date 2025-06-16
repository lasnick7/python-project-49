from ..cli import welcome_user, end_of_the_game
from ..games.even_game import even_game


def main():
    name = welcome_user()
    game_result = even_game()
    end_of_the_game(name, *game_result)


if __name__ == '__main__':
    main()
