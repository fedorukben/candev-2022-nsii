#!/usr/bin/env python
# type: ignore
import bokeh as bk
import bokeh.plotting

x = [1,2,3,4,5]
y = [1,4,9,16,25]

fig = bk.plotting.figure(title='Line Plot Example',
                         x_axis_label='x',
                         y_axis_label='y')
fig.line(x,y)
bk.io.show(fig)
