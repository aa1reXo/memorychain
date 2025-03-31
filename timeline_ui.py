import plotly.express as px
import pandas as pd

def render_timeline(memories):
    if not memories:
        return px.scatter(title="No memories yet")
    df = pd.DataFrame(memories)
    df['start'] = pd.to_datetime(df['timestamp'])
    df['end'] = df['start']
    fig = px.timeline(df, x_start='start', x_end='end', y='summary', hover_data=['transcript'])
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    return fig
