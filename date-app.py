#Misija ir uztaisīt jauno aplikāciju priekš jauniem pāriem, lai tas būtu interesantāks nekā Tinder!


import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("Dating App")
window.geometry("800x600")

# TODO: Add your GUI elements and mini-games here

# Start the application
window.mainloop()

# Function to open a mini-game window
def open_mini_game():
    mini_game_window = tk.Toplevel(window)
    mini_game_window.title("Mini Game")
    mini_game_window.geometry("400x300")
    # TODO: Add your mini-game GUI elements here

# Create a button to open the mini-game
mini_game_button = tk.Button(window, text="Play Mini Game", command=open_mini_game)
mini_game_button.pack()


#mini-game ping pong

import pygame
import random

# Initialize the game
pygame.init()

# Set up the game window
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping Pong Game")

# Define colors
WHITE = (255, 255, 255)

# Set up the game clock
clock = pygame.time.Clock()

# Define the paddles
paddle_width = 10
paddle_height = 60
paddle_speed = 5
left_paddle_x = 50
left_paddle_y = window_height // 2 - paddle_height // 2
right_paddle_x = window_width - 50 - paddle_width
right_paddle_y = window_height // 2 - paddle_height // 2

# Define the ball
ball_size = 10
ball_speed_x = 3
ball_speed_y = 3
ball_x = window_width // 2 - ball_size // 2
ball_y = window_height // 2 - ball_size // 2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < window_height - paddle_height:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < window_height - paddle_height:
        right_paddle_y += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with paddles
    if ball_x <= left_paddle_x + paddle_width and left_paddle_y <= ball_y + ball_size <= left_paddle_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)
    if ball_x >= right_paddle_x - paddle_width and right_paddle_y <= ball_y + ball_size <= right_paddle_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= window_height - ball_size:
        ball_speed_y = -ball_speed_y

    # Ball out of bounds
    if ball_x < 0 or ball_x > window_width:
        ball_x = window_width // 2 - ball_size // 2
        ball_y = window_height // 2 - ball_size // 2
        ball_speed_x = random.choice([-3, 3])
        ball_speed_y = random.choice([-3, 3])

    # Update the game window
    window.fill(WHITE)
    pygame.draw.rect(window, WHITE, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(window, WHITE, (ball_x, ball_y, ball_size, ball_size))
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit the game
pygame.quit()

#mini-game sudoku

import random

# Function to generate a Sudoku grid
def generate_sudoku():
    grid = [[0] * 9 for _ in range(9)]
    solve_sudoku(grid)
    return grid

# Function to solve the Sudoku grid using backtracking
def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

# Function to find an empty cell in the grid
def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None

# Function to check if a number is a valid move at a given position
def is_valid_move(grid, row, col, num):
    # Check row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

# Function to display the Sudoku grid
def display_sudoku(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# Function to play the Sudoku game
def play_sudoku():
    grid = generate_sudoku()
    display_sudoku(grid)

# Start the game
play_sudoku()