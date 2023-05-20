import sys
sys.stdin = open("input.txt", "r")
# 10
print(" ")
for test_case in range(1, 11):
    dump = int(input())
    box = list(map(int,input().split()))
    box.sort(reverse=True)
    for i in range(dump):
        if box[0] - box[-1] > 1:
            box[0] -= 1
            box[-1] += 1
            box.sort(reverse=True)
            continue
        elif box[0] - box[-1] <= 1:
            break

    print(f'#{test_case}', box[0] - box[-1])


