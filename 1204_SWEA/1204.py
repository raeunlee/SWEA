from collections import Counter

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    test_case_num = int(input())
    score = list(map(int, input().split()))
    cnt = Counter(score)
    best = cnt.most_common(1)
    print(f'#{test_case_num}',best[0][0])