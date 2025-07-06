# app.py

import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="무선 충전 시뮬레이터", layout="centered")

st.title("📱 무선 충전 위치 최적화 시뮬레이터")
st.markdown("""
전자기 유도 기반 무선 충전 시스템에서 **충전 거리**와 **코일 정렬도**가 충전 효율에 어떤 영향을 주는지 시뮬레이션합니다.
""")

# 입력 값
distance = st.slider("송신 코일과 수신 코일 간 거리 (cm)", 1, 50, 10)
alignment = st.slider("코일 정렬도 (0~100%)", 0, 100, 100)

# 효율 계산: (정렬도 × 1/d^2) × 100
efficiency = (alignment / 100) * (1 / (distance ** 2)) * 100

st.subheader(f"🔋 추정 충전 효율: **{efficiency:.2f}%**")

# Plotly 그래프 생성
x = np.linspace(1, 50, 200)
y = (alignment / 100) * (1 / (x ** 2)) * 100

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='충전 효율(%)'))
fig.add_vline(x=distance, line=dict(color="red", dash="dash"), name="현재 거리")
fig.update_layout(
    title="거리 vs 충전 효율",
    xaxis_title="거리 (cm)",
    yaxis_title="충전 효율 (%)",
    template="plotly_white"
)

st.plotly_chart(fig)
