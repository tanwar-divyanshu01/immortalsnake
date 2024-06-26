from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 150
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "#C5B4E3"
FOOD_COLOR = "#FFFFFF"
BACKGROUND_COLOR = "#000000"
AXE = 0

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)



class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH//SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT//SPACE_SIZE)-1) * SPACE_SIZE
        # UNLOCK THE INFINITE SNAKE EATER BY UNCOMMENTING THE FOLLOWING CODE and COMMETING THE X AND Y LINES ABOVE
        # global AXE
        # garb, AXE = divmod(AXE+1,(GAME_WIDTH//SPACE_SIZE)-1)
        # x = AXE * SPACE_SIZE
        # y = 5*SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x,y,x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag = "food")
        
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    if y >= GAME_WIDTH:
        y = 0
    
    if x < 0:
        x = ((GAME_WIDTH//SPACE_SIZE)-1) * SPACE_SIZE
    
    if y < 0:
        y = ((GAME_HEIGHT//SPACE_SIZE)-1) * SPACE_SIZE
    
    if x >= GAME_WIDTH:
        x = 0

    snake.coordinates.insert(0, (x,y))

    square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global SPEED

        SPEED -= 2
        
        global score 

        score += 10

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    window.after(SPEED, next_turn, snake, food)
        

def change_direction(new_direction):
    global direction
    
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

window = Tk()
window.title("Immortal snake")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Snake's hungry!".format(score), font=('consolas', 12))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<a>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<d>', lambda event: change_direction('right'))
window.bind('<w>', lambda event: change_direction('up'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<s>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()



