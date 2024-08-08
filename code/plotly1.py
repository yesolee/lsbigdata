# !pip install plotly

import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
import numpy as np

df_covid19_100=pd.read_csv("./data/df_covid19_100.csv")
df_covid19_100.info()

fig = go.Figure(
    data = {"type": "scatter",
         "mode": "markers",
         "x": df_covid19_100.loc[df_covid19_100["iso_code"]=="KOR", "date"],
         "y": df_covid19_100.loc[df_covid19_100["iso_code"]=="KOR", "new_cases"],
         "marker": {"color": "red"}
         }
)
fig.show()

# p.26 마진 변수 설정
margins_P = {"l": 25, "r": 25, "t": 50, "b": 50}
fig = go.Figure(
    data = [
        {
            "type": "scatter",
            "mode": "markers",
            "x": df_covid19_100.loc[df_covid19_100["iso_code"]=="KOR", "date"],
            "y": df_covid19_100.loc[df_covid19_100["iso_code"]=="KOR", "new_cases"],
            "marker": {"color": "red"}
        },
        {
            "type": "scatter",
            "mode": "lines",
            "x": df_covid19_100.loc[df_covid19_100["iso_code"]=="KOR", "date"],
            "y": df_covid19_100.loc[df_covid19_100["iso_code"]=="KOR", "new_cases"],
            "line": {"color": "blue", "dash": "dash"}
        }
    ],
    layout= {
        "title": "코로나 19 발생현황",
        "xaxis": {"title": "날짜", "showgrid": False},
        "yaxis": {"title": "확진자수"},
        "margin": margins_P
    }
)
fig.show()

#프레임속성========
# 애니메이션 프레임 생성
frames = []
dates = df_covid19_100.loc[df_covid19_100["iso_code"] == "KOR", "date"].unique()

for date in dates:
    frame_data = {
        "data": [
            {
                "type": "scatter",
                "mode": "markers",
                "x": df_covid19_100.loc[(df_covid19_100["iso_code"] == "KOR") & (df_covid19_100["date"] <= date), "date"],
                "y": df_covid19_100.loc[(df_covid19_100["iso_code"] == "KOR") & (df_covid19_100["date"] <= date), "new_cases"],
                "marker": {"color": "red"}
            },
            {
                "type": "scatter",
                "mode": "lines",
                "x": df_covid19_100.loc[(df_covid19_100["iso_code"] == "KOR") & (df_covid19_100["date"] <= date), "date"],
                "y": df_covid19_100.loc[(df_covid19_100["iso_code"] == "KOR") & (df_covid19_100["date"] <= date), "new_cases"],
                "line": {"color": "blue", "dash": "dash"}
            }
        ],
        "name": str(date)
    }
    frames.append(frame_data)

# 애니메이션을 위한 레이아웃 설정
margins_P = {"l": 25, "r": 25, "t": 50, "b": 50}
layout = {
    "title": "코로나 19 발생현황",
    "xaxis": {"title": "날짜", "showgrid": False},
    "yaxis": {"title": "확진자수"},
    "margin": margins_P,
    "updatemenus": [{
        "type": "buttons",
        "showactive": False,
        "buttons": [{
            "label": "Play",
            "method": "animate",
            "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}]
        }, {
            "label": "Pause",
            "method": "animate",
            "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}]
        }]
    }]
}

# Figure 생성
fig = go.Figure(
    data=[
        {
            "type": "scatter",
            "mode": "markers",
            "x": df_covid19_100.loc[df_covid19_100["iso_code"] == "KOR", "date"],
            "y": df_covid19_100.loc[df_covid19_100["iso_code"] == "KOR", "new_cases"],
            "marker": {"color": "red"}
        },
        {
            "type": "scatter",
            "mode": "lines",
            "x": df_covid19_100.loc[df_covid19_100["iso_code"] == "KOR", "date"],
            "y": df_covid19_100.loc[df_covid19_100["iso_code"] == "KOR", "new_cases"],
            "line": {"color": "blue", "dash": "dash"}
        }
    ],
    layout=layout,
    frames=frames
)

fig.show()

