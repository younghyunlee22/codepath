def find_longest_consonant_substring(str):
    substring = ""
    maxsub = 0
    vowels = "aeiou"
    for char in str:
        if char not in vowels:
            substring += char
            if maxsub < len(substring):
                maxsub = len(substring)
        else:  # 이 부분을 제대로 처리 못했음
            substring = ""

    return maxsub


print(find_longest_consonant_substring("helloworld"))

# the longest xxx: two pointer, sliding window로 풀 수 있어야 함

# Create a function that takes in an integer n and returns n!

# Examples:
# --------
# Input: 3
# Output: 6

# Input: 5
# Output: 120


def factorial_iterative(n):  # O(N)
    n_factorial = 1

    for i in range(2, n + 1):
        n_factorial *= i

    return n_factorial


print(factorial_iterative(3))


def factorial_recursive(n):  # O(N)
    if n == 1:  # Base Case
        return n
    else:  # Recursive Step
        return n * factorial_recursive(n - 1)


print(factorial_recursive(3))
