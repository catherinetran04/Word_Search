#Catherine Tran

import random
import string


def get_size(grid):
    """get the size of word search"""
    i = len(grid)
    j = len(grid[0])
    temp = (j, i)
    return temp


def print_word_grid(grid):
    """"print the grid"""
    for i in grid:
        for j in i:
            print(j, end="")
        print()


def copy_word_grid(grid):
    """make a copy of the grid"""
    outer = []
    for i in grid:
        inner = []
        for j in i:
            inner.append(j)
        outer.append(inner)
    return outer


def extract(grid, position, direction, max_len):
    """find word given answer location adn direction"""
    temp = ""
    if max_len == 0:
        return temp
    for i in range(max_len):
        x = position[0] + (i * direction[0])
        y = position[1] + (i * direction[1])
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
            temp = temp + (grid[y][x])
    return temp


def show_solution(grid, word, solution):
    """change answer to caps"""
    if not solution:
        print(word, "is not found in this word search")
    else:
        sol = copy_word_grid(grid)
        for i in range(len(word)):
            x = (solution[0][0] + (i * solution[1][0]))
            y = (solution[0][1] + (i * solution[1][1]))
            sol[y][x] = sol[y][x].upper()

        print(word.upper(), "can be found as below")
        for i in sol:
            for j in i:
                print(j, end="")
            print()


def find(grid, word):
    """find the word"""
    right = (1, 0)
    down = (0, 1)
    right_down = (1, 1)
    right_up = (1, -1)
    directions = (right, down, right_down, right_up)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in directions:
                sol = ""
                for l in range(len(word)):
                    x = (i + (l * k[0]))
                    y = (j + (l * k[1]))
                    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                        sol = sol + (grid[y][x])
                if sol == word:
                    location = (i, j)
                    solution = (location, k)
                    return solution
    return False


def find_all(grid, words):
    """find all words"""
    temp = {}
    for i in range(len(words)):
        temp[words[i]] = find(grid, words[i])
    return temp


def generate(width, height, words):
    """generate a word search"""
    words_found = []
    right = (1, 0)
    down = (0, 1)
    right_down = (1, 1)
    right_up = (1, -1)
    directions = (right, down, right_down, right_up)
    grid = []
    for i in range(height):
        inner = []
        for j in range(width):
            inner.append("")
        grid.append(inner)

    for i in words:
        for j in range(100):
            valid = False
            x0 = random.randrange(height)
            y0 = random.randrange(width)
            d = random.randrange(4)
            for k in range(len(i)):
                x = x0 + (k * directions[d][0])
                y = y0 + (k * directions[d][1])
                if (0 <= y < width) and (0 <= x < height):
                    temp = grid[y][x]
                    if (temp == i[k:(k+1)]) or (temp == ""):
                        valid = True
            if valid:
                for k in range(len(i)):
                    x = x0 + (k * directions[d][0])
                    y = y0 + (k * directions[d][1])
                    grid[y][x] = i[k:(k+1)]
                words_found.append(i)
                break


    for i in range(width):
        for j in range(height):
            if grid[j][i] == "":
                x = random.choice(string.ascii_letters)
                grid[j][i] = x.lower()

    temp = (grid, words_found)
    return temp

if __name__ == "__main__":
    x = generate(5, 10, ['cat', 'dog', 'art', 'town', 'den', 'wolf', 'part', 'mansion'])
    for i in x:
        for j in i:
            print(j)
