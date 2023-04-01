def find_sum(matrix):
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result += matrix[i][j]
    return result

s, e = map(int, input().split())
matrix = [[]] * s

for i in range(s):
    matrix[i] = list(map(int, input().split()))
    
print(find_sum(matrix))
    
