# img/2.10-11.2.png

import numpy as np
import matplotlib.pyplot as plt

plots = [
    {
        'func': lambda x: (1 + x) / (1 - x),
        'range': (-5, 0),
        'title': '(1 + x) / (1 - x)',
        'color': 'blue'
    },
    {
        'func': lambda x: np.sin(np.sqrt(x)),
        'range': (0, 5),
        'title': 'np.sin(np.sqrt(x))',
        'color': 'red'
    },
    {
        'func': lambda x: np.arctan(1 / x),
        'range': (-1, 1),
        'title': 'np.arctan(1 / x)',
        'color': 'green'
    },
    {
        'func': lambda x: np.log(x - 1 / x) ** 2,
        'range': (2, 9),
        'title': 'np.log(x - 1 / x) ** 2',
        'color': 'purple'
    }
]

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for i, plot in enumerate(plots):
    x = np.linspace(plot['range'][0], plot['range'][1], 500)
    
    y = plot['func'](x)
    
    axes[i].plot(x, y, color=plot['color'], label=plot['title'])
    axes[i].set_title(plot['title'])
    axes[i].grid(True, linestyle='-')
    axes[i].axhline(y=0, color='black', linewidth=0.5)
    axes[i].axvline(x=0, color='black', linewidth=0.5)
    
plt.show()
