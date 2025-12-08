import turtle
import pandas
from pandas.io.stata import stata_epoch

correctStates = 0

pandasDF = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandasDF.get("state").tolist()

iteration = 0

lastFeedback = "Welcome to the game!"
while correctStates < 50:
    playerInput = screen.textinput("50 States Game", lastFeedback + "\n\nGuess a State Name:")
    if playerInput in states:
        lastFeedback = f"Good Job! {playerInput} is a state!"
        states.pop(states.index(playerInput))
        correctStates += 1

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = pandasDF[pandasDF.state == playerInput]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(playerInput)

    else:
        lastFeedback = f"Sorry, you might've guessed {playerInput}, or {playerInput} is not a state, or the spelling/capitalization of {playerInput} is not correct. Please try again."
screen.textinput("50 States Game!", "Congrats! You have now completed the map, and guessed all 50 States! Once you close this dialog, the window will close, so please go ahead and admire your work.")