"""https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

Result
  https://app.codility.com/demo/results/trainingT9JRZZ-FAZ/

Task Score 100%
Correctness 100%
Performance 100%
"""
def solution(X, Y, D):
    distance = Y - X
    if distance % D == 0: return distance // D
    else: return distance // D + 1
