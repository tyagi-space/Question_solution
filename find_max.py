# Original lists: [1, 2, 4, 3, 5, 4, 6, 9, 2, -10]
# Maximum sum sub-sequence of the said list: 36
#sequence = [1, 2, -4, 3, 5, 4, 6, 9, 2, -10] = 28



def find_max(sequence):
    max =  0
    sum = 0
    for i in sequence:
        sum += i
        if sum > max:
            max = sum

    return max     
sequence = [1, 2, 4, 3, 5, -24, 6, 9, -2]
max = find_max(sequence)
print(max)