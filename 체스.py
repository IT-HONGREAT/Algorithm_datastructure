n,m = map(int,input().split())

chess = []
for _ in range(n):
    chess.append(input())
print(chess)

answer = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

def checker(n):
    wrong = 0
    for i in range(8):

        if n[0][i] != answer[0][i]:
            wrong += 1
        if n[1][i] != answer[1][i]:
            wrong += 1
        if n[2][i] != answer[2][i]:
            wrong += 1
        if n[3][i] != answer[3][i]:
            wrong += 1
        if n[4][i] != answer[4][i]:
            wrong += 1
        if n[5][i] != answer[5][i]:
            wrong += 1
        if n[6][i] != answer[6][i]:
            wrong += 1
        if n[7][i] != answer[7][i]:
            wrong += 1
    return wrong

save_wrong = []
for i in range(n-8+1):

    before_save_wrong = 0

    for j in range(m-8+1):
        right = chess[j:j+9]
        checker(right)
        before_save_wrong += 1

