def count_occurrences(arr, k):
    result = []
    for i in arr:
        if arr.count(i) == k:
            result.append(i)
    return set(result)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
occurrences = sorted(list(count_occurrences(arr, k)))
if occurrences:
    for i in occurrences:
        print(i, end=' ')
else:
    print(0)
