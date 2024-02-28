import random
import math

N = int(input())  # カードの枚数
A = [0] * N  # 各カードの表面の数値
B = [0] * N  # 各カードの裏面の数値

for i in range(N):
    A[i], B[i] = map(int, input().split())

# 目標値
target = 5 * 10**17

# 初期温度、終了温度、冷却率
T0 = 1000
Tf = 1
alpha = 0.999

def evaluate(A, B, target):
    """評価関数：カード1の表裏の数値と目標値との差の絶対値の和"""
    return abs(A[0] - target) + abs(B[0] - target)

def simulated_annealing(A, B, T0, Tf, alpha, max_operations=50):
    operations = []
    T = T0
    current_score = evaluate(A, B, target)
    while T > Tf and len(operations) < max_operations:
        # ランダムに2枚のカードを選択
        u, v = random.sample(range(N), 2)
        # 操作を試みる
        new_A_u, new_A_v = (A[u] + A[v]) // 2, (A[u] + A[v]) // 2
        new_B_u, new_B_v = (B[u] + B[v]) // 2, (B[u] + B[v]) // 2
        # 一時的に更新
        A[u], A[v], B[u], B[v] = new_A_u, new_A_v, new_B_u, new_B_v
        new_score = evaluate(A, B, target)
        delta = new_score - current_score
        if delta < 0 or random.random() < math.exp(-delta / T):
            # 更新を確定
            current_score = new_score
            operations.append((u+1, v+1))
        else:
            # 更新を取り消し
            A[u], A[v], B[u], B[v] = A[u], A[v], B[u], B[v]
        # 温度の更新
        T *= alpha
    return operations

operations = simulated_annealing(A, B, T0, Tf, alpha)

# 出力
print(len(operations))
for u, v in operations:
    print(u, v)


print(abs(A[0] - target) + abs(B[0] - target))