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
    teamWins = [0, 0]  # American League, Natl. League win counts
    gameNumber = 0
    while gameNumber < 7:
        gameNumber += 1
        wsg = np.random.randint(1, 5 + 1)
        if wsg < 4:
            teamWins[0] += 1
        else:
            teamWins[1] += 1
        if teamWins[0] == 4 or teamWins[1] == 4:
            if teamWins[0] == 4:
                winner = "AL"
            else:
                winner = "NL"
    return teamWins[0] + teamWins[1], winner


# Run the simulation
# Repeat for a large number of trials (World Series), in this case 10000
for i in range(10000):
    gamesAndWinners.append(declareWinner())
print(gamesAndWinners)

# Analyze the results
# find the counts of each (How many times did it take 4, 5, 6, 7 games to win?)
# this uses a list comprehension to populate the list of games played per series
gamesPlayedToWin = [x[0] for x in gamesAndWinners]
print(np.bincount(gamesPlayedToWin))
# Graph your results for better visualization
# fivethirty eight, bmh; grayscale, dark_background, ggplot
import matplotlib.pyplot as plt

plt.style.use("ggplot")
plt.figure(figsize=(10, 5))
plt.hist(gamesPlayedToWin)
plt.title("Number of Games in World Series")
plt.ylabel("Frequency of World Series Length")
plt.xlabel("Number of Games Played")
plt.show()
# find the average number of games it took for one team to win the World Series
print(np.average(gamesPlayedToWin))
# Now add code to find out how many times the American League team won compared to the National League team.
winningTeam = [x[1] for x in gamesAndWinners]
values, counts = np.unique(winningTeam, return_counts=True)
print(values, counts)
type(winningTeam)
# What other questions might you want to ask? What else do you want to learn?
