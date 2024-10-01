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
            ["e", "h", "e", "a", "h", "t"],
            ["h", "r", "v", "f", "l", "g"],
            ["g", "t", "y", "e", "o", "i"],
            ["r", "n", "a", "x", "r", "b"],
            ["b", "e", "i", "i", "u", "c"],
            ["a", "n", "s", "m", "t", "e"],
            ["l", "t", "a", "l", "e", "r"],
            ["e", "d", "d", "i", "m", "w"],
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
