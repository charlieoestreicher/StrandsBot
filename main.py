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
            ["H", "S", "F", "O", "N", "I"],
            ["K", "A", "U", "A", "P", "O"],
            ["O", "Q", "S", "L", "U", "N"],
            ["H", "L", "H", "L", "M", "P"],
            ["R", "A", "E", "N", "I", "K"],
            ["A", "S", "R", "L", "P", "P"],
            ["B", "H", "I", "V", "A", "T"],
            ["I", "D", "A", "R", "E", "S"],
        ]
    else:
        grid = fetch_daily_grid()

    grid = [[letter.lower() for letter in row] for row in grid]

    # Solve the puzzle
    solutions = solve_strands(grid)

    # Display the solutions
    display_solutions(solutions)

    logger.info("NYT Strands bot finished.")


if __name__ == "__main__":
    main()
