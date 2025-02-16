from brain_games.games.core_brain_even import RULES, game_logic_even
from brain_games.engine import c_brain_games


# Старт игры.
def main():
    c_brain_games(RULES, game_logic_even)
    

if __name__ == "__main__":
    main()
       