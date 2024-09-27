from config.logger import logger
from .strands_tile import Tile
from .trie import Trie


trie = Trie.create_trie()


def get_neighbors(tile, grid):
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]
    neighbors = [
        Tile(tile.x + dx, tile.y + dy, grid[tile.x + dx][tile.y + dy])
        for dx, dy in directions
        if 0 <= tile.x + dx < len(grid[0]) and 0 <= tile.y + dy < len(grid[1])
    ]
    return neighbors


def is_valid_word(word):
    if len(word) < 4 or not trie.is_prefix_or_word(word):
        return False
    logger.info(f"found a word {word}")
    return True


def find_all_words(tile, word, grid, visited):
    # if not is_prefix(word):
    #     return []
    neighbors = get_neighbors(tile, grid)
    visited.append(tile)
    ret = []
    if is_valid_word(word):
        ret.append(word)
    for nbr in neighbors:
        potential_word = word + nbr.letter
        if nbr not in visited:
            found_words = find_all_words(nbr, potential_word, grid, visited)
            ret.extend(found_words)
    visited.remove(tile)
    return ret


# make visited a set and add to it that way
# make grid much smaller like 'cat'


def solve_strands(grid):
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            tile = Tile(x, y, letter)
            all_words = find_all_words(tile, tile.letter, grid, [tile])
            print(all_words)
    logger.info("body of solve_strands")
