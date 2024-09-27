from bot.strands_fetcher import fetch_daily_grid
from bot.strands_solver import solve_strands
from bot.strands_display import display_solutions
from config.logger import logger
import enchant
from bot.trie import Trie

env = "d"


def main():
    logger.info("NYT Strands bot starting")

    # Fetch the daily grid
    if env == "d":
        grid = [
            ["I", "R", "C", "I"],
            ["R", "B", "T", "S"],
            ["E", "L", "O", "R"],
            ["L", "A", "H", "I"],
        ]
    else:
        grid = fetch_daily_grid()

    t = Trie.create_trie()

    # Solve the puzzle
    solutions = solve_strands(grid)

    # Display the solutions
    display_solutions(solutions)

    logger.info("NYT Strands bot finished.")


if __name__ == "__main__":
    main()
