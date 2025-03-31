from brain_games.games.gcd import RULES, game_logic_gcd
from brain_games.engine import c_brain_games


def main():
    c_brain_games(RULES, game_logic_gcd)


if __name__ == "__main__":
    main()