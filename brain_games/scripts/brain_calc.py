#!/usr/bin/env python3


from brain_games.games.calc import RULES, game_logic_calc
from brain_games.engine import c_brain_games


def main():
    c_brain_games(RULES, game_logic_calc)


if __name__ == "__main__":
    main()