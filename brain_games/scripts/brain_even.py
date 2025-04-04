from brain_games.games.even import RULES, check_even
from brain_games.engine import launch_brain_game


# Старт игры.
def main():
    launch_brain_game(RULES, check_even)
    

if __name__ == "__main__":
    main()
