from brain_games.games.calc import RULES, calculate_operation
from brain_games.engine import launch_brain_game


def main():
    launch_brain_game(RULES, calculate_operation)


if __name__ == "__main__":
    main()