from plotly.offline import plot as opy
import plotly.graph_objs as go
from .models import *
import pandas as pd


def example_graph():
    x_data = [0, 1, 2, 3]
    y_data = [x**2 for x in x_data]
    plot_div = opy([go.Scatter(x=x_data, y=y_data,
                               mode='lines', name='test',
                               opacity=0.8)],
                   output_type='div')

    return plot_div


def latest_three_year_peak_backup_overlap():
    df = pd.DataFrame(list(DailyPeakBackup.objects.all().values()))
    print(df)

    fig = go.Figure()

    for year in range(2010, 2022):
        try:
            data = df[df['time'].dt.year == year]
            print(data)
            if len(data) == 0:
                continue

            fig.add_trace(go.Scatter(x=data.time.dt.day_of_year, y=data.backup_volume_rate,
                                     mode='lines+markers',
                                     name=f'{year}', opacity=0.8))
        except Exception as e:
            print(e)
    try:
        plot_div = opy(fig,
                       output_type='div')
        return plot_div
    except Exception as e:
        print(e)

    return False


def powerplant_graph():
    df = pd.DataFrame(list(PowerPlantSuppportHistory.objects.all().values()))
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df[df[""]]))
