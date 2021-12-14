
import sys

player_1_choice = 'x'
player_2_choice = 'o'
game_draw = 'DRAW'


# Define grid


# We will use list comprehension to  create 3 * 3 grid

grid = [cell for cell in range(9)]


# let us create a function that displays a grid


def display_grid():

    print(f"{grid[0]} {grid[1]} {grid[2]}")
    print(f"{grid[3]} {grid[4]} {grid[5]}")
    print(f"{grid[6]} {grid[7]} {grid[8]}")


# lets call display_grid function





# let's write  a function that will check winning condtion and

def check_winner():

    # Check the rows

    if grid[0]  == grid[1] == grid[2]:
        return grid[0]
    elif grid[3] == grid[4] == grid[5]:
        return grid[3]
    elif grid[6]  == grid[7] == grid[8]:
        return grid[6]

    # check for cols
    elif grid[0] == grid[3] == grid[6]:
        return grid[0]
    elif grid[1] == grid[4] == grid[7]:
        return grid[1]
    elif grid[2] == grid[5] == grid[8]:
        return grid[2]
    # check for diagonal

    elif grid[2] == grid[4]  == grid[6]:
        return grid[2]

    elif grid[0] == grid[4]  == grid[8]:
        return grid[2]

    # check for draw.
    else:
        for cell in grid:
            if isinstance(cell,int):
                # Game is ongoinh yet not finished
                # Do nothing
                # just return
                return

        return game_draw


# let's create a game function that will call
# check_winner function and return the condtion of a game

def game():
    winner = check_winner()


    if winner == 'x':
        print("X: is the winner")
        display_grid()
        sys.exit

    elif winner == 'o':
        print("O: is the winner")
        display_grid()
        sys.exit()

    elif winner == game_draw:
        print("Game is draw")
        sys.exit()


# Now lets create a function that will validate the player input
# And check if the location of the grid are
# already occupied ask for another input
# function will be update_grid

def update_grid(choice, location):
    """
    Choice: 'x' or 'o'
    location: (0 to 8)
    """

    if location < 0 or location > 9:

        raise ValueError("Not a valid location")

    if grid[location] == 'x' or grid[location] == 'o':
        raise ValueError("Location already filled with", grid[location])


    # if none f the condition true
    # User input is a valid
    else:
        grid[location] = choice

# No let's create a main function
# that will call the game and upgrade_grid function
# and ask for the player input

def main():
    player_1_location = int(
        input("Player [x] Enter your choice from (0 t 8)"))
    # pass player 1 location choice using upgrade_grid function

    update_grid(player_1_choice, player_1_location)

    # After upgrading check thw winning, loosing or draw condition
    # by calling game function
    game()
    display_grid()

    player_2_location = int(
    input("Player [o] Enter your choice from (0 to 8)"))
    # pass player 2 location choice using upgrade_grid function
    update_grid(player_2_choice, player_2_location)
    game()
    display_grid()


# our main function complete
# Now time to run the main function inside while loop continuosly

display_grid()

while True:
    main()


