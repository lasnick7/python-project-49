from ..cli import welcome_user, end_of_the_game
from ..games.prime_game import prime_game


def main():
    name = welcome_user()
    game_result = prime_game()
    end_of_the_game(name, *game_result)


if __name__ == '__main__':
    main()
