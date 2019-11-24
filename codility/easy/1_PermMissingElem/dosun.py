"""https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

Result:
  https://app.codility.com/demo/results/training3ZEF8B-Y9D/
  Find the missing element in a given permutation.
Task Score  : 100%
Correctness : 100%
Performance : 100%
"""
def solution(A):
    return sum(range(len(A) + 2)) - sum(A)
