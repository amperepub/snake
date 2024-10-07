import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(master, width=600, height=400, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = None
        self.direction = 'Right'
        self.score = 0

        self.create_food()
        self.draw_snake()
        self.master.bind("<Key>", self.change_direction)
        self.move_snake()

    def create_food(self):
        while True:
            x = random.randint(0, 59) * 10
            y = random.randint(0, 39) * 10
            self.food = (x, y)
            if self.food not in self.snake:  # Ensure food is not on the snake
                break
        self.canvas.create_oval(x, y, x + 10, y + 10, fill="red", tag="food")

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", tag="snake")

    def change_direction(self, event):
        if event.keysym == 'Up' and self.direction != 'Down':
            self.direction = 'Up'
        elif event.keysym == 'Down' and self.direction != 'Up':
            self.direction = 'Down'
        elif event.keysym == 'Left' and self.direction != 'Right':
            self.direction = 'Left'
        elif event.keysym == 'Right' and self.direction != 'Left':
            self.direction = 'Right'

    def move_snake(self):
        x, y = self.snake[0]

        if self.direction == 'Up':
            y -= 10
        elif self.direction == 'Down':
            y += 10
        elif self.direction == 'Left':
            x -= 10
        elif self.direction == 'Right':
            x += 10

        new_head = (x, y)

        # Check for collision with walls or self
        if (x < 0 or x >= 600 or y < 0 or y >= 400 or new_head in self.snake):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        # Check if the snake has eaten the food
        if new_head == self.food:
            self.score += 1
            self.canvas.delete("food")
            self.create_food()  # Create new food
        else:
            self.snake.pop()  # Remove the last segment of the snake

        self.draw_snake()
        self.master.after(100, self.move_snake)  # Move the snake every 100 milliseconds

    def game_over(self):
        self.canvas.create_text(300, 200, text="Game Over", fill="white", font=("Arial", 30))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
