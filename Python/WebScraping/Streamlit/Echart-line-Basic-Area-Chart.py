# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:29:34 2024

@author: Shin

"""
# https://echarts.streamlit.app/
# pip install streamlit_echarts

import streamlit as st
import streamlit_echarts as echarts

options = {
  "xAxis": {
    "type": 'category',
    "boundaryGap": False,
    "data": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  "yAxis": {"type": "value"},
  "series": [
    {
      "data": [150, 230, 224, 218, 135, 147, 260],
      "type": "line",
      "areaStyle": {},
    }
  ]
}
echarts.st_echarts(options=options)


