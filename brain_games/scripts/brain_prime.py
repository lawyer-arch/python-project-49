from brain_games.games.prime import RULES, prime_number_check
from brain_games.engine import calculate_operation


def main():
    calculate_operation(RULES, prime_number_check)


if __name__ == "__main__":
    main()