# question 17
def largest_cube_LE(k):
    i = 1
    ans = 1
    while True:
        i += 1
        candidate = i ** 3
        if candidate <= k:
            ans = candidate
        else:
            return ans

print(largest_cube_LE(10**5 + 1))