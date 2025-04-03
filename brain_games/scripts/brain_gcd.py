from brain_games.games.gcd import RULES, find_the_divisor
from brain_games.engine import launch_brain_game


def main():
    launch_brain_game(RULES, find_the_divisor)


if __name__ == "__main__":
    main()