from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iterations = 10000
results = np.zeros(iterations)
change_mind = True
prize = ''

# Loop for the specified iterations...
for i in range(iterations):
    doors = np.array(['car', 'goat', 'goat'], dtype="U30")
    np.random.shuffle(doors)
    chosen_door = randint(0, 2)

    if change_mind:
        doors[chosen_door] = 'selected'
        doors = np.sort(doors)

        # So now we have our chosen door. 
        prize = doors[0]
    else:
        prize = doors[chosen_door]

    # Have we guessed correctly? If so, update the results array.
    if prize.startswith('car'):
        results[i] = 1

# Create a dataframe from the numpy array.
ds = pd.DataFrame(results, columns=['Score'])
ds['Mean'] = ds['Score'].expanding().mean()

if change_mind:
    title = 'Decide to change mind  ' + str(ds.iloc[iterations-1, 1])
else:
    title = 'Stick with 1st choice ' + str(ds.iloc[iterations-1, 1])   



# Plot the results.
ds['Mean'].plot()
plt.title(title)
plt.xlabel('Number of guesses')
plt.ylabel('Average correct guesses')
plt.legend(loc='lower right')
plt.show()























