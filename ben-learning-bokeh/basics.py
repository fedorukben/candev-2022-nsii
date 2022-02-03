# type: ignore
import bokeh as bk
import bokeh.plotting as bplt

p = bplt.figure(plot_width = 600, plot_height = 600,
                       title = 'Example Glyphs',
                       x_axis_label = 'X', y_axis_label = 'Y')

squares_x = [1, 3, 4, 5, 8]
squares_y = [8, 7, 3, 1, 10]
circles_x = [9, 12, 4, 3, 15]
circles_y = [8, 4, 11, 6, 10]

p.square(squares_x, squares_y, size = 12, color = 'navy', alpha = 0.5)
p.circle(circles_x, circles_y, size = 12, color = 'red')

bk.io.show(p)
