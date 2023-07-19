# A jagged list is a 2D list where the sublist are of different lengths. Write a function called is_jagged() that takes a single parameter, a 2D list called lst. If the 2D list is jagged, return True. Otherwise, False.

# Input: [[1,2,3], [4,5,6,7], [8, 9,10]]
# Output: True

# Input: [[1,2,3], [4,5,6], [7,8,9]]
# Output: False


def is_jagged(lst):
  for i in range(len(lst) -1):
    if len(lst[i]) != len(lst[i+1]):
      return True
  return False

print(is_jagged([[1,2,3], [4,5,6], [7,8,9]]))

#teacher's code
def is_jagged_list(lst):
  # Find the length of the first row
  num_cols = len(lst[0]) 
  # Iterate over the rows.
  for i in range(1, len(lst)):
    
    # If any of the rows are a different length, return True.
    if len(lst[i]) != num_cols:
      return True
    return False

ratings =  [ [5, 3, 4],
             [5, 5, 4],
             [4, 5, 4] ]
for row in ratings:
  for col in row:
     print(col, end = ' ')

