from brain_games.games.prime import RULES, prime_number_check
from brain_games.engine import launch_brain_game


def main():
    launch_brain_game(RULES, prime_number_check)


if __name__ == "__main__":
    main()