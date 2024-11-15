n = int(input())
m = int(input())

set_1 = set(map(int, input().split()))

set_2 = set(map(int, input().split()))

intersection = sorted(set_1 & set_2)

print(intersection)
