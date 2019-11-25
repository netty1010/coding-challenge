"""https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

result 
  https://app.codility.com/demo/results/trainingV9VU6Y-4JQ/
  
Task Score  : 75%
Correctness : 83%
Performance : 66%
"""
def solution(A):
    result = sum(range(len(A) + 1)) - sum(A)
    if result == 0: return 1
    else: return 0
