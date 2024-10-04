
# Word Search Puzzle Generator and Solver

## Overview

This program generates a word search puzzle grid, with an option to either use default settings or customize the grid size and word list. Words are randomly placed in various directions, and the grid is filled with random letters where no words are present. You can also view the solution with the words highlighted.

## Features

- **Default Grid Size**: The grid is 10 columns wide and 5 rows tall by default.
- **Default Word List**: If no customization is made, the following words are used: `['cat', 'dog', 'art', 'town', 'den', 'wolf', 'part', 'mansion']`.
- **Customizable Grid and Words**: You can input a custom grid size and provide your own list of words.
- **Random Word Placement**: Words are placed randomly in 8 possible directions (horizontally, vertically, and diagonally).
- **Random Filler Letters**: The remaining empty cells are filled with random lowercase letters.
- **Solution Display**: After generating the word search, you can opt to display the solution, where found words are highlighted.

## How It Works

1. **Word Placement**: Words can be placed in 8 directions: right, left, up, down, and four diagonal directions.
2. **Random Filler Letters**: After placing all words, remaining spaces are filled with random letters.
3. **Solution Finder**: The program finds and highlights the placed words upon request.

## Usage

### Prerequisites

- Python 3.x

### Running the Program

1. Save the code into a Python file (e.g., `word_search.py`).
2. Run the script:
   ```bash
   python word_search.py
   ```

### Example

When you run the program, you'll be asked if you want to customize the grid or use the default settings:

- **Default grid size**: 10 (width) x 5 (height)
- **Default word list**: `['cat', 'dog', 'art', 'town', 'den', 'wolf', 'part', 'mansion']`

If you choose to customize:
- **Grid size**: Enter the width and height of your choice.
- **Word list**: Input words separated by commas.

After generating the puzzle, you can type 'S' to display the solutions.

#### Sample Output

```
Do you want to customize grid size and words? (yes/no): no
Generated Word Search Grid:

btfartpuco
pdogenhmpo
catdqxgjkl
oneloyhlim
wionstrmal

Words placed: ['cat', 'dog', 'art', 'town', 'den', 'wolf', 'part', 'mansion']

If you wish to see the solutions to the search type 'S': s

CAT can be found as below:
btfartpuco
pdogenhmpo
CATdqxgjkl
oneloyhlim
wionstrmal
```

### Functions

1. **`generate(width, height, words)`**: Generates a word search grid with the specified width, height, and words.
2. **`find(grid, word)`**: Searches for a given word in the grid in all 8 possible directions.
3. **`find_all(grid, words)`**: Searches for all words and returns their positions.
4. **`show_solution(grid, word, solution)`**: Highlights the word in the grid and prints it.
5. **`print_word_grid(grid)`**: Displays the word search grid.

## Customization

The program gives you the option to either use the default grid size (10x5) and word list or customize both:

- **Default Settings**:
  - Width: `10`
  - Height: `5`
  - Words: `['cat', 'dog', 'art', 'town', 'den', 'wolf', 'part', 'mansion']`

To use custom settings, answer "yes" when prompted, and you can input:
- **Custom grid size**: Choose your preferred width and height.
- **Custom word list**: Provide a comma-separated list of words.
