import numpy as np
import matplotlib.pyplot as plt

# Try to reproduce the figure shown in images/exercise_1-2.png
# Here's the data and colors used.

t = np.linspace(0, 2 * np.pi, 150)
x1, y1 = np.cos(t), np.sin(t)
x2, y2 = 2 * x1, 2 * y1

colors = ['darkred', 'darkgreen']

# Try to plot the two circles, scale the axes as shown and add a legend
# Hint: it's easiest to combine `ax.axis(...)` and `ax.margins(...)` to scale
# the axes
