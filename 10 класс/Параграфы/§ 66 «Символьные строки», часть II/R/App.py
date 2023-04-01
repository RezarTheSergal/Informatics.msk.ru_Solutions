def get_used_digits(string, array):
    for i in range(len(string)):
        if string[i].isdigit() and int(string[i]) in dictionary:
            if int(string[i]) not in array:
                array.append(int(string[i]))
    return array


def pop_used_digits(array, dictionary):
    for num in array:
        if num in dictionary:
            index = dictionary.index(num)
            dictionary.pop(index)
    return dictionary


def print_minimal_integer(left_dict):
    if len(left_dict) > 0:
        for integer in left_dict:
            print(integer, end='')
    else:
        print(0)
        return

             
string = input()
dictionary = list(range(1, 10))

print_minimal_integer(pop_used_digits(get_used_digits(string, list()), dictionary))
