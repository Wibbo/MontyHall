from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iterations = 1000
results = np.zeros(iterations)

for i in range(iterations):
    doors = np.array(['car', 'goat', 'goat'])
    np.random.shuffle(doors)
    my_door_index = randint(0, 2)

    if doors[my_door_index] == 'car':
        results[i] = 1

ds = pd.DataFrame(results, columns=['Score'])
ds['Mean'] = ds['Score'].expanding().mean()
print(ds)

ds['Mean'].plot()
plt.title('Single door, one choice')
plt.xlabel('Number of guesses')
plt.ylabel('Average correct guesses')
plt.legend(loc='lower right')
plt.show()




















