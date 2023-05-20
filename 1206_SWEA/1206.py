import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1,11):
    result = 0
    buildings = int(input())
    buildings_height = list(map(int , input().split()))
    for i in range(2, buildings-2):
        def_2 = buildings_height[i] - buildings_height[i-2]
        def_1 = buildings_height[i] - buildings_height[i-1]
        def1 = buildings_height[i] - buildings_height[i+1]
        def2 = buildings_height[i] - buildings_height[i+2]
        if def_2 > 0 and def_1 > 0 and def1 > 0 and def2 > 0 :
            result += min(def_2, def_1, def1, def2)
    print(f'#{test_case}', result)