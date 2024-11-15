def max_bush(n, a):
    max_sum = 0

    for i in range(n):
        cur_sum = a[i]
        if i == 0:
            cur_sum += a[n - 1] + a[(i + 1) % n]
        elif i == n - 1:

            cur_sum += a[i - 1] + a[0]
        else:
            cur_sum += a[i - 1] + a[i + 1]

        max_sum = max(max_sum, cur_sum)
    return max_sum


n = int(input())
a = list(map(int, input().split()))

print(max_bush(n, a))
