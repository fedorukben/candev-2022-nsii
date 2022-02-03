# type: ignore
import bokeh as bk
import bokeh.plotting as bplt
import numpy as np
import pandas as pd

flights = pd.read_csv('flights.csv')

arr_hist, edges = np.histogram(flights['arr_delay'],
                               bins=int(180 / 5),
                               range=[-60, 120])
delays = pd.DataFrame({'flights': arr_hist,
                       'left': edges[:-1],
                       'right': edges[1:]})
delays['f_interval'] = ['%d to %d minutes' % (left, right) for left, right in zip(delays['left'], delays['right'])]

src = bk.models.ColumnDataSource(delays)
print(src.data.keys())

fig = bplt.figure(plot_height=600, plot_width=600,
                  title="Histogram of Arrival Delays with Inspectors",
                  x_axis_label="Delay (min)",
                  y_axis_label="Number of Flights")

fig.quad(source=src, bottom=0, top='flights',
         left='left', right='right',
         fill_color='red', line_color='black', fill_alpha=0.75,
         hover_fill_alpha=1.0, hover_fill_color='navy')

hover = bk.models.HoverTool(tooltips=[('Delay', '@f_interval'),
                                      ('(x,y)', '($x,$y)')])
# @ takes from the ColumnDataSource (similar to DataFrame)
# $ takes from the plot itself (such as x and y)

fig.add_tools(hover)

bk.io.show(fig)
