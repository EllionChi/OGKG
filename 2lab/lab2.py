import pandas as pd
import matplotlib.pyplot as plt

file_path = 'DS1.txt' 

data = pd.read_csv(file_path, sep=' ', header=None, names=['x', 'y'])

canvas_width, canvas_height = 960, 540

plt.figure(figsize=(canvas_width / 100, canvas_height / 100))

plt.scatter(data['x'], data['y'])

plt.savefig('result.png', dpi=100)
plt.show()
