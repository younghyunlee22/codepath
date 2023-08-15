# Given a list lst with 0s and 1s, find the count of the maximum number of consecutive 1s present in the list

# Example:

# Input: lst = [1, 1, 1, 0, 1]
# Output: 3

# Input: lst = [0, 1, 0, 1, 1, 0, 0]
# Output: 2

#my code
def max_consecutive(lst):
    count = 1
    max = 0
    for i in range(len(lst) - 1):
        if lst[i] == 1 and lst[i + 1] == 1:
            count += 1
        curr_max = count
    if curr_max > max:
        max = curr_max
        
    return max

print(max_consecutive([1, 1, 1, 0, 1]))

#teacher's code
def consecutive_ones(lst):
    max_count = 0
    curr_count = 0
    for num in lst:
        if num == 1:
            curr_count += 1
        else:
            curr_count = 0

        if curr_count > max_count:
            max_count = curr_count

    return max_count


print(consecutive_ones([1, 1, 1, 0, 1]))
print(consecutive_ones([0, 1, 0, 1, 1, 0, 0]))
print(consecutive_ones([0]))
print(consecutive_ones([1]))
print(consecutive_ones([1, 0]))
print(consecutive_ones([0, 1]))


# A1: Write a function total_inventory, which takes two inventory dictionaries and a key and gives the total count of the item from both inventory lists. Make sure it doesn’t produce an error if the item isn’t in the inventory lists (in this case assume the value is 0).

# Example
# --------
# Input: {"bananas": 5, "apples": 3}, {"bananas": 2}, "bananas"
# Output: 7


def total_inventory(inventory1, inventory2, item):
  inv1 = int(inventory1.get(item, 0))
  inv2 = int(inventory2.get(item, 0))
  return inv1 + inv2

print(total_inventory({"bananas": 5, "apples": 3}, {"bananas": 2}, "bananas"))

# A2: Write a function translate which takes a list of words in one language and a translation dictionary, and uses the translation dictionary to return a list of words in the second language.

# Example
# -------
# Input: ["hello", "world"], {"hello": "hola", "world": "mundo"}
# Output: ["hola", "mundo"]


def translate(words, dictionary):
  result = []
  for word in words:
    result.append(dictionary[word])

  return result

print(translate(["hello", "world"], {"hello": "hola", "world": "mundo"}))

