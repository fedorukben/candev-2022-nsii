# type: ignore
import bokeh as bk
import bokeh.plotting as bplt
import numpy as np
import pandas as pd

flights = pd.read_csv('flights.csv')
print(flights['arr_delay'].describe())

arr_hist, edges = np.histogram(flights['arr_delay'],
                               bins = int(180 / 5),
                               range = [-60, 120])
delays = pd.DataFrame({'flights': arr_hist,
                       'left': edges[:-1],
                       'right': edges[1:]})

print(flights.head())

fig = bplt.figure(plot_height = 600, plot_width = 600,
             title = "Histogram of Arrival Delays",
             x_axis_label = "Delay (min)",
             y_axis_label = "Number of Flights")

# Add quad glyph
fig.quad(bottom = 0, top = delays['flights'],
         left = delays['left'], right = delays['right'],
         fill_color = 'red', line_color = 'black')

bk.io.show(fig)
