import streamlit as st
import pandas as pd
import copy
import random as rd

# カードの初期状態を設定（例として3枚のカードを用意）
N = 3

# 表面の値をランダムに45個生成
A = [rd.randint(10**17, 10**18) for _ in range(N)] 
# 裏面の値をランダムに45個生成
B = [rd.randint(10**17, 10**18) for _ in range(N)] 

# カードの状態を保存するリスト
states = [(copy.deepcopy(A), copy.deepcopy(B))]

# カードの状態をビジュアライズする関数
def visualize_cards(A, B, step):
    df = pd.DataFrame({'Front': A, 'Back': B})
    st.write(f'Card Values at Step {step}')
    st.bar_chart(df)

# 操作をシミュレート
def operate_cards(A, B, u, v):
    A[u], A[v] = (A[u] + A[v]) // 2, (A[u] + A[v]) // 2
    B[u], B[v] = (B[u] + B[v]) // 2, (B[u] + B[v]) // 2
    states.append((copy.deepcopy(A), copy.deepcopy(B)))


# 例として、ランダムなカード2枚を選んだ操作を50回行う
for _ in range(50):
    u, v = rd.sample(range(N), 2)
    operate_cards(A, B, u, v)


# stepごとのカードの状態をスライダーで表示
step = st.slider('Step', 0, len(states)-1, 0)

# スライダーを操作すると、カードの状態が変わる
A_step, B_step = states[step]
visualize_cards(A_step, B_step, step)