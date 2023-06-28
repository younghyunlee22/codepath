# 1. mean()
def mean(arr):
    sum = 0
    for num in arr:
        sum += num
        mean = sum / len(arr)
    return mean

print(mean([3,4,5]))

# 2. three_consecutive_nums()

numlist = [1, 5, 2, 2, 3, 4, 2]

def three_consecutive_nums(arr):
    left = 0
    right = 1
    if len(arr) < 3:
        return False
    else:
        for i in arr:
            if arr[left] == arr[right]:
                right += 1
                if arr[left] == arr[right]:
                    return True
                else:
                    return False
            else:
                left += 1
                right += 1
print(three_consecutive_nums(numlist))

#3. three_consecutive_twos

