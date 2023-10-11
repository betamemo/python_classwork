# Write a function returns a list with digits of a given number
# Input: 123
# Output: [1, 2, 3]

def solution(n):
    n = str(n)
    l = list(n)
    for i in range(0, len(l)):
        l[i] = int(l[i])
    return l


print(solution(123))
