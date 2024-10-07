import curses
import random

# Set up the window
stdscr = curses.initscr()
curses.curs_set(0)  # Hide the cursor
sh, sw = stdscr.getmaxyx()  # Get height and width of window
w = curses.newwin(sh, sw, 0, 0)  # Create a new window
w.keypad(1)  # Enable keypad mode
w.timeout(100)  # Refresh every 100 milliseconds

# Initialize the snake and food
snk_x = sw // 4  # Initial x position of the snake
snk_y = sh // 2  # Initial y position of the snake
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]
food = [sh // 2, sw // 2]  # Initial position of food
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)  # Place food on the window

key = curses.KEY_RIGHT  # Initial direction

# Game loop
while True:
    next_key = w.getch()  # Get user input
    key = key if next_key == -1 else next_key  # Update the direction based on input

    # Calculate new head position of the snake
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Check if snake hits the wall or itself
    if (new_head[0] in [0, sh] or
        new_head[1] in [0, sw] or
        new_head in snake):
        curses.endwin()  # End the window
        quit()

    snake.insert(0, new_head)  # Add new head to the snake

    # Check if snake eats the food
    if snake[0] == food:
        food = None
        while food is None:  # Generate new food position
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(int(food[0]), int(food[1]), curses.ACS_PI)  # Place new food
    else:
        # Remove the last segment of the snake
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    # Render the snake
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

# Clean up
curses.endwin()
