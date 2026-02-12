import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data
lp = pd.read_csv('10_project_data_lineplots.csv')

# Create 2x3 subplot grid
fig, axs = plt.subplots(2, 3, figsize=(20, 10))

ylim = [0, 24]

# Function to format y-axis as percentage
def format_as_percentage(x, pos):
    return f'{int(x)}%'

columns = ['A', 'B', 'C', 'D', 'E', 'F']

for ax, col in zip(axs.flatten(), columns):
    ax.plot(lp['years'], lp[col], linewidth=4)
    ax.set_ylim(ylim)
    ax.set_title(col)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.grid(axis='y')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(format_as_percentage))

plt.tight_layout()
plt.show()