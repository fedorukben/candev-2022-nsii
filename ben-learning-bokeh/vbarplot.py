# type: ignore
import bokeh as bk
import bokeh.plotting

fig = bk.plotting.figure(plot_width=200, plot_height=400)
fig.vbar(x=[1,2,3], width=0.5, bottom=0, top=[2,4,6], color='Cyan')
bk.io.show(fig)
