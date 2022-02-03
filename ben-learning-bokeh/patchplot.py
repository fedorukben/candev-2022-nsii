import bokeh as bk
import bokeh.plotting

xs = [[5,3,4], [2,4,3], [2,3,5,4]]
ys = [[6,4,2], [3,6,7], [2,4,7,8]]

fig = bk.plotting.figure()
fig.patches(xs, ys, fill_color=['red','blue','black'], line_color='white')

bk.io.show(fig)
