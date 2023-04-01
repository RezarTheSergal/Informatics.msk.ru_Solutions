def count_exact_amount(matrix, a):
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == a:
                result += 1
    return result

s, e = map(int, input().split())
matrix = [[]] * s

for i in range(s):
    matrix[i] = list(map(int, input().split()))

key_finder = int(input())
print(count_exact_amount(matrix, key_finder))
