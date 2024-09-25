from bot.strands_fetcher import fetch_daily_grid
from bot.strands_solver import solve_strands
from bot.strands_display import display_solutions
from config.logger import logger

env = "d"


def main():
    logger.info("NYT Strands bot starting")

    # Fetch the daily grid
    if env == "d":
        grid = [
            ["R", "A", "M", "S", "I", "L"],
            ["I", "T", "C", "N", "E", "A"],
            ["A", "N", "I", "O", "B", "O"],
            ["O", "E", "N", "R", "E", "T"],
            ["I", "R", "D", "C", "F", "I"],
            ["D", "R", "G", "U", "M", "C"],
            ["B", "O", "T", "A", "I", "T"],
            ["Y", "C", "N", "T", "O", "N"],
        ]
    else:
        grid = fetch_daily_grid()

    # Solve the puzzle
    solutions = solve_strands(grid)

    # Display the solutions
    display_solutions(solutions)

    logger.info("NYT Strands bot finished.")


if __name__ == "__main__":
    main()
