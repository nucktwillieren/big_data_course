from plotly.offline import plot as opy
import plotly.graph_objs as go


def example_graph():
    x_data = [0, 1, 2, 3]
    y_data = [x**2 for x in x_data]
    plot_div = opy([go.Scatter(x=x_data, y=y_data,
                               mode='lines', name='test',
                               opacity=0.8, marker_color='green')],
                   output_type='div')

    return plot_div
