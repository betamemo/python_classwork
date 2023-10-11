def solution(n):
    ch = ['A', 'B', 'C', 'D', 'E',
          'F', 'G', 'H', 'I', 'J',
          'K', 'L', 'M', 'N', 'O',
          'P', 'Q', 'R', 'S', 'T',
          'U', 'V', 'W', 'X', 'Y', 'Z']

    if n <= 26:
        return ch[n - 1]
    elif n % 26 == 0:
        return solution((n // 26) - 1) + solution(n % 26)
    else:
        return solution(n // 26) + solution(n % 26)


for i in range(1, 703):
    print(i, '=', solution(i))
