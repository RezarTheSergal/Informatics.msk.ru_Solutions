def get_string(data):
    for i in range(len(elements)):
        data = data.replace(str(i+1), elements[i])
    return data
    

def get_permutations(n, k):
    elements = list(range(1, n+1))
    permutations = []
    used = [False] * n 

    def backtrack(current_permutation):
        if len(current_permutation) == k:
            permutations.append(current_permutation)
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                backtrack(current_permutation + [elements[i]])
                used[i] = False
            
    backtrack([])
    sorted_permutations = sorted(permutations)
    for perm in sorted_permutations:
        print(get_string(''.join(map(str, perm))))
    print(len(sorted_permutations)) 

string = input()
elements = [char for char in string]
get_permutations(len(string), int(input()))
