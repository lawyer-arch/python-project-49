from brain_games.games.progression import RULES, get_progression_string
from brain_games.engine import launch_brain_game


def main():
    launch_brain_game(RULES, get_progression_string)


if __name__ == "__main__":
    main()