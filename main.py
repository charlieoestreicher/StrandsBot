from bot.strands_fetcher import fetch_daily_grid
from bot.strands_solver import solve_strands
from bot.strands_display import display_solutions
from config.logger import logger


def main():
    logger.info("starting")

    # Fetch the daily grid
    grid = fetch_daily_grid()

    # Solve the puzzle
    solutions = solve_strands(grid)

    # Display the solutions
    display_solutions(solutions)

    logger.info("NYT Strands bot finished.")


if __name__ == "__main__":
    main()
