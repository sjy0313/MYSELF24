# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:49:13 2024

@author: Shin
"""

# data download site: 
# https://echarts.apache.org/examples/data/asset/data/les-miserables.json
# Echarts 아래 data 폴더안에 les_miserables.json (webpage저장)


import streamlit_echarts as echarts
import json

with open("./les-miserables.json", "r") as f:
    graph = json.loads(f.read())

for idx, node in enumerate(graph["nodes"]):
    graph["nodes"][idx]["label"] = {"show": node["symbolSize"] > 30}

option = {
    "title": {
        "text": "Les Miserables",
        "subtext": "Default layout",
        "top": "bottom",
        "left": "right",
    },
    "tooltip": {},
    "legend": [{"data": [a["name"] for a in graph["categories"]]}],
    "animationDuration": 1500,
    "animationEasingUpdate": "quinticInOut",
    "series": [
        {
            "name": "Les Miserables",
            "type": "graph",
            "layout": "none",
            "data": graph["nodes"],
            "links": graph["links"],
            "categories": graph["categories"],
            "roam": True,
            "label": {"position": "right", "formatter": "{b}"},
            "lineStyle": {"color": "source", "curveness": 0.3},
            "emphasis": {"focus": "adjacency", "lineStyle": {"width": 10}},
        }
    ],
}
echarts.st_echarts(option, height="500px")


