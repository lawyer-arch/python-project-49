#!/usr/bin/env python3


from brain_games.games.game_core_brain_progression import (RULES,
                                                           game_logic_progression)
from brain_games.engine import c_brain_games


def main():
    c_brain_games(RULES, game_logic_progression)


if __name__ == "__main__":
    main()