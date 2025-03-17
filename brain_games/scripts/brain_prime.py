#!/usr/bin/env python3


from brain_games.games.core_brain_prime import RULES, game_logic_prime
from brain_games.engine import c_brain_games


def main():
    c_brain_games(RULES, game_logic_prime)


if __name__ == "__main__":
    main()