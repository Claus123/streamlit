import streamlit as st
import pandas as pd
import copy

# ユーザーにカードの値を一括で入力させる
cards_input = st.text_area('Enter the front and back values for each card, separated by spaces (e.g., "A1 B1 A2 B2 ... AN BN"):')

# 操作の詳細を入力させる
operations_input = st.text_area('Enter the number of operations followed by each pair of card numbers for the operations, separated by spaces (e.g., "X u1 v1 u2 v2 ... uX vX"):')

def parse_operations(input_str):
    """入力された操作の文字列をパースして、操作回数とカードペアのリストを返す"""
    items = list(map(int, input_str.split()))
    num_operations = items[0]
    pairs = [(items[i], items[i+1]) for i in range(1, len(items), 2)]
    return num_operations, pairs

if cards_input and operations_input:
    values = list(map(int, cards_input.split()))
    A = values[0::2]
    B = values[1::2]
    N = len(A)
    states = [(copy.deepcopy(A), copy.deepcopy(B))]
    
    num_operations, operations = parse_operations(operations_input)
    
    # 操作をシミュレート
    def operate_cards(A, B, u, v):
        A[u], A[v] = (A[u] + A[v]) // 2, (A[u] + A[v]) // 2
        B[u], B[v] = (B[u] + B[v]) // 2, (B[u] + B[v]) // 2
        states.append((copy.deepcopy(A), copy.deepcopy(B)))
    
    # ユーザーが入力した操作をシミュレート
    for u, v in operations:
        operate_cards(A, B, u-1, v-1)  # ユーザーが1から数えるためにインデックスを調整
    
    # カードの状態をビジュアライズする関数
    def visualize_cards(A, B):
        df = pd.DataFrame({'Front': A, 'Back': B})
        st.bar_chart(df)
    
    # ステップごとのカードの状態をスライダーで表示
    if len(states) > 1:
        step = st.slider('Step', 0, len(states)-1, 0)
        A_step, B_step = states[step]
        visualize_cards(A_step, B_step)
        
        # このステップにおけるV1 + V2の計算
        V1 = abs(A_step[0] - 5*10**17)
        V2 = abs(B_step[0] - 5*10**17)
        sum_V1_V2 = V1 + V2
        st.write(f"V1 + V2 at Step {step}: {sum_V1_V2}")
else:
    st.write("Please enter card values and operations above.")
