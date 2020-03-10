# World Series Simulation
# American League baseball team is considered to have a 60% chance of beating the National League team in any given World Series game.
# In the World Series, how often will the American League win? And how many games will it typically take?

# Model: Generate a random integer between 1 and 5 to simulate a World Series game played; 1, 2, 3 will represent an American League team win and 4, 5 will represent a National League team win
# Trial: Generate random integers between 1 and 5 until either 4 numbers between 1 and 3 or 4 numbers between 4 and 5 are generated.
# Statistic of Interest: The number of games played until a winner is declared (either 4, 5, 6 or 7 games)

# import the numpy package
import numpy as np
gamesAndWinners = []
# function to probabilistically 'play' the games and declare a winner
def declareWinner():
    teamwins = [0, 0] # American League, Natl. League win counts

# Run the simulation
# Repeat for a large number of trials (World Series), in this case 10000


# Analyze the results
# find the counts of each (How many times did it take 4, 5, 6, 7 games to win?)
# this uses a list comprehension to populate the list of games played per series


# Graph your results for better visualization


#fivethirty eight, bmh; grayscale, dark_background, ggplot




# find the average number of games it took for one team to win the World Series


# Now add code to find out how many times the American League team won compared to the National League team.



# What other questions might you want to ask? What else do you want to learn?