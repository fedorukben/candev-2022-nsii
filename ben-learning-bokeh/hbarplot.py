# type: ignore
import bokeh as bk
import bokeh.plotting

fig = bk.plotting.figure(plot_width=400, plot_height=200)
fig.hbar(y=[2,4,6], height=1, left=0, right=[1,2,3], color='Cyan')
bk.io.show(fig)
