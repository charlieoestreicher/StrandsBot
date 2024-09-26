from bot.strands_fetcher import fetch_daily_grid
from bot.strands_solver import solve_strands
from bot.strands_display import display_solutions
from config.logger import logger

env = "d"


def main():
    logger.info("NYT Strands bot starting")

    # Fetch the daily grid
    if env == "d":
        grid = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    else:
        grid = fetch_daily_grid()

    # Solve the puzzle
    solutions = solve_strands(grid)

    # Display the solutions
    display_solutions(solutions)

    logger.info("NYT Strands bot finished.")


if __name__ == "__main__":
    main()
