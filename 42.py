# Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd
import numpy as np
data = pd.read_csv('sample_data/california_housing_train.csv')
min_population = data['population'].min() 
filtered_data = data[data['population'] == min_population]
max_households = np.max(filtered_data['households'])
print("Максимальное количество households для зоны с минимальным значением population: ", max_households)