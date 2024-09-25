class Letter:
    def __init__(self, value, id):
        self.value = value
        self.id = id


def get_all_paths(letter):
    
    


def create_dictionary_trees(grid):
    char_dic = {}
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            letter = Letter(grid[row][col], (row, col))
            char_dic[letter] = get_all_paths(letter)


def solve_strands(grid):
    create_dictionary_trees(grid)
    print("hello")
