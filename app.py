# app.py

import streamlit as st

st.set_page_config(page_title="무선 충전 시뮬레이터", layout="centered")

st.title("📱 무선 충전 위치 최적화 시뮬레이터")
st.markdown("""
전자기 유도 기반 무선 충전 시스템에서 **충전 거리**와 **코일 정렬도**가 충전 효율에 어떤 영향을 주는지 시뮬레이션합니다.
""")

# 사용자 입력
distance = st.slider("송신 코일과 수신 코일 간 거리 (cm)", min_value=1, max_value=50, value=10)
alignment = st.slider("코일 정렬도 (완벽 정렬=100%)", min_value=0, max_value=100, value=100)

# 효율 계산 (간단한 물리 모델: 정렬도 * (1 / 거리^2))
efficiency = (alignment / 100) * (1 / (distance ** 2)) * 100

st.subheader(f"🔋 현재 충전 효율 추정: **{efficiency:.2f}%**")

# 간단한 효율 테이블 출력
st.markdown("---")
st.markdown("### 📊 거리별 충전 효율 비교표")

st.write("| 거리(cm) | 충전 효율(%) |")
st.write("|----------|----------------|")
for d in range(1, 51, 5):
    e = (alignment / 100) * (1 / (d ** 2)) * 100
    st.write(f"| {d} | {e:.2f} |")

# 텍스트 기반 시각화 (막대 표현)
st.markdown("---")
st.markdown("### 📈 텍스트 기반 충전 효율 시각화")
for d in range(1, 26, 2):
    e = (alignment / 100) * (1 / (d ** 2)) * 100
    bar = "█" * int(e / 2)
    st.write(f"{d:2}cm: {bar} {e:.2f}%")
