from brain_games.games.gcd import RULES, find_the_divisor
from brain_games.engine import calculate_operation


def main():
    calculate_operation(RULES, find_the_divisor)


if __name__ == "__main__":
    main()