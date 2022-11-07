from turtle import *

from freegames import line

# welcome message when game is started
print("Welcome to 4wins!")
print("the rules:")
print("1. You can only place a stone in a column that is not full.")
print("2. You can only put a stone in the lowest row of a column. ")
print("3. You can only win if you have 4 stones in a row, column or diagonal.")

# function to draw the board
turns = {'red': 'yellow', 'yellow': 'red'}
state = {'player': 'yellow', 'rows': [0] * 8}


def grid():
    bgcolor('light blue')

    for x in range(-150, 200, 50):
        line(x, -200, x, 200)

    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            up()
            goto(x, y)
            dot(40, 'white')

    update()


def tap(x, y):
    """Draw red or yellow circle in tapped row."""
    player = state['player']
    rows = state['rows']

    row = int((x + 200) // 50)
    count = rows[row]

    x = ((x + 200) // 50) * 50 - 200 + 25
    y = count * 50 - 200 + 25

    up()
    goto(x, y)
    dot(40, player)
    update()

    rows[row] = count + 1
    state['player'] = turns[player]


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(tap)
done()
print(row)


# detect if a player won the game


def check_winner():
    # check rows
    for i in range(0, 8):
        if state['rows'][i] == 4:
            print("Player " + state['player'] + " won the game!")
            return True
    # check collumns
