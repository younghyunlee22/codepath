def max_sum(lst):
    max_sum = 0

    for row in lst:
        sum = 0
        for num in row:
            sum += num

        if sum > max_sum:
            max_sum = sum

    return max_sum


lst = [[0, 0, 1], [1, 1, 1], [4, 0, 0]]
assert max_sum(lst) == 4

lst = [[100, 200, 300], [100, 200, 0], [200, 200, 200]]
assert max_sum(lst) == 600
