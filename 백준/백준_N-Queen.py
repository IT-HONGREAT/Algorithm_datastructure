"""
input : 8

output : 92

"""

def is_available(candidate, column):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == column or abs(candidate[queen_row] - column) == current_row - queen_row:
            return False

    return True



def DFS(N, current_row, current_candidate, possible_list):

    if current_row == N:  # 현재 row가 제시한 숫자와 동일하면 끝 row이다.
        possible_list.append(current_candidate[:]) # 얕은복사
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col): # 후보군과 현재 열들을 받아서 사용할수 있는지 판단
            current_candidate.append(candidate_col)
            DFS(N, current_row+1, current_candidate, possible_list)
            current_candidate.pop()





def n_queens(N):

    possible_list = []
    DFS(N, 0, [], possible_list)
    return possible_list

print(len(n_queens(8)))