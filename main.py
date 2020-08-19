from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iterations = 10000
change_results = np.zeros(iterations)
stay_results = np.zeros(iterations)

# change_mind = True
change_prize = ''
stay_prize = ''

# Loop for the specified iterations...
for i in range(iterations):
    change_doors = np.array(['car', 'goat', 'goat'], dtype="U30")
    stay_doors = np.array(['car', 'goat', 'goat'], dtype="U30")

    np.random.shuffle(change_doors)
    np.random.shuffle(stay_doors)   
    chosen_door = randint(0, 2)

    change_doors[chosen_door] = 'selected'
    change_doors = np.sort(change_doors)
    change_prize = change_doors[0]

    stay_prize = stay_doors[chosen_door]

    # Have we guessed correctly? If so, update the results array.
    if change_prize.startswith('car'):
        change_results[i] = 1

    if stay_prize.startswith('car'):
        stay_results[i] = 1

# Create a dataframe from the numpy array.
df_change = pd.DataFrame(change_results, columns=['Score'])
df_change['Mean'] = df_change['Score'].expanding().mean()

df_stay = pd.DataFrame(stay_results, columns=['Score'])
df_stay['Mean'] = df_stay['Score'].expanding().mean()

plt.title('The Monty Hall problem')
plt.xlabel('Number of guesses')
plt.ylabel('Average correct guesses')
ax = df_change['Mean'].plot(label='Changed mind')
df_stay['Mean'].plot(ax = ax, label='Did not change mind')
plt.legend(loc='lower right')
plt.show()
























