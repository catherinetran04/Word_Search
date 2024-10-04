
import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import string

# Define directions as constants for better readability
DIRECTIONS = {
    "right": (1, 0),
    "down": (0, 1),
    "right_down": (1, 1),
    "right_up": (1, -1),
    "left": (-1, 0),
    "up": (0, -1),
    "left_down": (-1, 1),
    "left_up": (-1, -1)
}

# Word Search Helper Functions
def generate(width, height, words):
    """Generate a word search grid with the given words."""
    grid = [["" for _ in range(width)] for _ in range(height)]
    words_found = []

    for word in words:
        placed = False
        for _ in range(100):  # Attempt to place the word 100 times
            start = (random.randrange(width), random.randrange(height))
            direction = random.choice(list(DIRECTIONS.values()))
            if can_place_word(grid, word, start, direction):
                place_word(grid, word, start, direction)
                words_found.append(word)
                placed = True
                break

        if not placed:
            print(f"Could not place the word: {word}")

    # Fill empty cells with random letters
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "":
                grid[y][x] = random.choice(string.ascii_lowercase)

    return grid, words_found

def can_place_word(grid, word, start, direction):
    """Check if a word can be placed at a given position and direction."""
    for i in range(len(word)):
        x = start[0] + i * direction[0]
        y = start[1] + i * direction[1]
        if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            return False
        if grid[y][x] not in ("", word[i]):
            return False
    return True

def place_word(grid, word, start, direction):
    """Place the word in the grid at the given position and direction."""
    for i in range(len(word)):
        x = start[0] + i * direction[0]
        y = start[1] + i * direction[1]
        grid[y][x] = word[i]

def find(grid, word):
    """Find the word in the grid in all possible directions."""
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for direction in DIRECTIONS.values():
                if extract(grid, (x, y), direction, len(word)) == word:
                    return (x, y), direction
    return False

def find_all(grid, words):
    """Find all words in the grid."""
    return {word: find(grid, word) for word in words}

def extract(grid, position, direction, max_len):
    """Extract a word from the grid given its start position and direction."""
    word = []
    for i in range(max_len):
        x = position[0] + (i * direction[0])
        y = position[1] + (i * direction[1])
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
            word.append(grid[y][x])
        else:
            break
    return "".join(word)

def show_solution(grid, word, solution):
    """Highlight the found word in the grid."""
    sol_grid = copy_word_grid(grid)
    if solution:
        for i in range(len(word)):
            x = solution[0][0] + (i * solution[1][0])
            y = solution[0][1] + (i * solution[1][1])
            sol_grid[y][x] = sol_grid[y][x].upper()  # Capitalize the solution letters for display
    return sol_grid

def copy_word_grid(grid):
    """Create a copy of the grid."""
    return [row[:] for row in grid]

# GUI Functions
def display_grid(window, grid):
    """Display the word search grid."""
    for widget in window.grid_slaves():
        if int(widget.grid_info()["row"]) < len(grid):
            widget.grid_forget()  # Remove any previous grid elements
    
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            label = tk.Label(window, text=letter, width= 1, height= 1, font=('Times New Roman', 18))
            label.grid(row=y, column=x)
            

def show_word_solution(grid, word, solution):
    """Show solution for a specific word in a new window."""
    sol_grid = show_solution(grid, word, solution)
    solution_window = tk.Toplevel()
    solution_window.title(f"Solution for {word.upper()}")

    # Create a black grid with black letters, except for the solution letters in red
    for y, row in enumerate(sol_grid):
        for x, letter in enumerate(row):
            color = "red" if letter.isupper() else "black"  # Red for solution letters
            label = tk.Label(solution_window, text=letter, font=('Times New Roman', 20), bg="white", fg=color)
            label.grid(row=y, column=x)

    # Set the background of the solution window to black
    solution_window.configure(bg="white")

def create_gui():
    """Create the GUI for the word search puzzle."""
    window = tk.Tk()
    window.title("Word Search Puzzle Generator")
    
    default_width = 10
    default_height = 5
    default_words = ['cat', 'dog', 'art', 'town', 'den', 'wolf', 'part', 'mansion']
    
    # Customization Option
    user_choice = messagebox.askyesno("Customize", "Do you want to customize the grid size and words?")
    
    if user_choice:
        width = simpledialog.askinteger("Grid Width", "Enter the grid width:", initialvalue=default_width)
        height = simpledialog.askinteger("Grid Height", "Enter the grid height:", initialvalue=default_height)
        words_input = simpledialog.askstring("Words", "Enter the words, separated by commas:",
                                             initialvalue="cat,dog,art,town,den,wolf,part,mansion")
        words = words_input.split(',')
    else:
        width = default_width
        height = default_height
        words = default_words
    
    grid, words_placed = generate(width, height, words)
    
    # Display the generated grid
    display_grid(window, grid)
    
    # Create a frame for words and buttons
    words_frame = tk.Frame(window)
    words_frame.grid(row=height + 1, columnspan=width)

    solutions = find_all(grid, words_placed)

    # Create buttons for each word
    words_found = tk.Label(words_frame, text= "Words placed and their solutions:", font=('Times New Roman', 20), bg = "black", fg = "pink")
    words_found.pack()

    for word in words_placed:

        word_button = tk.Button(words_frame, text=word, font=('Times New Roman', 14), bg= "lightgray", activeforeground="pink",
                                        command=lambda w=word: show_word_solution(grid, w, solutions[w]))
        word_button.pack(side=tk.LEFT, padx=5)

                                  

    window.mainloop()

if __name__ == "__main__":
    create_gui()
