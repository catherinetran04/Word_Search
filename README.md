# `Word Search Generator`

This project is a Python implementation of a word search generator. It allows you to generate a word search grid with words hidden in different directions. The grid is filled with random letters for empty spaces, and the hidden words can be searched and highlighted in the grid.
- Requirements: Python 3.x
No external libraries are required for this project. The standard random and string libraries are used.

- Running the Program: You can run the program directly from the command line:
```
python word_search.py
```

# Features
- Generates a grid of random letters with hidden words.
- Words are hidden in multiple directions (right, left, up, down, diagonals).
- Words are placed into the grid with up to 100 placement attempts for each word.
- Prints the generated word search grid.
- Finds the specified words within the grid and highlights them.
- Supports generating grids of any size.

# Directions
The program supports hiding words in the following 8 directions:
```
  Right: (1, 0)
  Down: (0, 1)
  Right-Down: (1, 1)
  Right-Up: (1, -1)
  Left: (-1, 0)
  Up: (0, -1)
  Left-Down: (-1, 1)
  Left-Up: (-1, -1)
```

# `Code Structure`
# Functions:
- get_size(grid): Returns the size of the grid as a tuple (width, height).
- print_word_grid(grid): Prints the current word search grid.
- copy_word_grid(grid): Creates and returns a copy of the grid.
- extract(grid, position, direction, max_len): Extracts a word from the grid given the starting position and direction.
- show_solution(grid, word, solution): Highlights the found word in the grid.
- find(grid, word): Searches for a word in all directions in the grid and returns its position and direction if found.
- find_all(grid, words): Searches for all words in the grid and returns their positions and directions.
- can_place_word(grid, word, start, direction): Checks if a word can be placed in the grid at a specific start position and direction.
- place_word(grid, word, start, direction): Places a word in the grid at the specified start position and direction.
- generate(width, height, words): Generates a word search grid with the given words and fills in the remaining cells with random letters.

# How to Use:
Generate Word Search Grid: The generate function is used to create a word search grid of any size with a specified list of words. For example, to create a grid of size 10x5 with some words, use the following call:

```
grid, words_placed = generate(10, 5, ['cat', 'dog', 'art', 'town', 'den', 'wolf', 'part', 'mansion'])
```
- Print the Grid: After generating the grid, you can print it using:
```
print_word_grid(grid)
```
- Find Words: To search for a specific word in the grid:
```
find(grid, 'dog')
```
- Show Solution: If the word is found, you can highlight its position in the grid using:
```
show_solution(grid, 'dog', find(grid, 'dog'))
```

# Example Output

```
Generated Word Search Grid:
c a t w o n t o w
o t x a r i a t f
g i t a i t o r m
d m w x n o n s i
e w u a q w l a p

Words placed: ['cat', 'dog', 'art', 'town', 'den', 'wolf', 'part', 'mansion']
```
