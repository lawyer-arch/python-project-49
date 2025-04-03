from brain_games.games.even import RULES, check_even
from brain_games.engine import calculate_operation


# Старт игры.
def main():
   calculate_operation(RULES, check_even)
    

if __name__ == "__main__":
    main()
