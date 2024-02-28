N = int(input())  # カードの枚数
A = [0] * N  # 各カードの表面の数値
B = [0] * N  # 各カードの裏面の数値

for i in range(N):
    A[i], B[i] = map(int, input().split())

# 目標値
target = 5 * 10**17

# 操作リスト
operations = []

def choose_best_pair(A, B, target):
    """目標値に最も近づけるペアを選択する"""
    best_diff = float('inf')
    best_pair = (0, 0)
    for i in range(1, N):
        diff_a = abs((A[0] + A[i]) // 2 - target)
        diff_b = abs((B[0] + B[i]) // 2 - target)
        avg_diff = (diff_a + diff_b) / 2
        if avg_diff < best_diff:
            best_diff = avg_diff
            best_pair = (i, avg_diff, diff_a, diff_b)
    return best_pair

for _ in range(50):  # 最大操作回数
    i, avg_diff, diff_a, diff_b = choose_best_pair(A, B, target)
    if avg_diff == float('inf'):  # 最適なペアが見つからない場合
        break
    # 表面と裏面の数値を更新
    A[0], A[i] = (A[0] + A[i]) // 2, (A[0] + A[i]) // 2
    B[0], B[i] = (B[0] + B[i]) // 2, (B[0] + B[i]) // 2
    operations.append((1, i + 1))

# 出力
print(len(operations))
for u, v in operations:
    print(u, v)

print(abs(A[0] - target) + abs(B[0] - target))
