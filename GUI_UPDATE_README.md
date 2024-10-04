# Word Search Puzzle Generator (Tkinter GUI Version)

## Overview

This project is a **Word Search Puzzle Generator** updated with a graphical interface built using Python's Tkinter library. Users can generate word search puzzles, interact with the grid to find solutions, and customize puzzle parameters such as grid size and words. This project allows for easy visual interaction and word-solving functionality.

## Features

1. **Puzzle Generation:**
   - Automatically generates a word search puzzle using a grid with random word placements in various directions.
   - Words are placed in the puzzle in random orientations: horizontally, vertically, or diagonally in any direction.

2. **Interactive Word Solution:**
   - Users can interact with the puzzle by clicking on the words.
   - Clicking a word displays a new window highlighting the location of that word in the puzzle, with letters shown in **red**.

3. **Customizable Puzzle Parameters:**
   - By default, a 10x5 grid is generated with pre-defined words: `['cat', 'dog', 'art', 'town', 'den', 'wolf', 'part', 'mansion']`.
   - Optionally, users can customize the grid size and input their own words via a simple input dialog.

4. **Word Finding:**
   - The program includes a solver function that finds the position of all words in the grid. Users can click buttons for each word to see the highlighted solution.

## Installation

1. Ensure that you have Python installed on your machine.
2. Install the Tkinter library if it is not already included (for most Python installations, Tkinter is included by default):
   ```bash
   pip install tk
