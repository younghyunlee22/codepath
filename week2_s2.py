char = input("Enter a single charater: ")
to_ascii = ord(char)
if 64 < to_ascii < 91:
    print('uppercase')
elif 96 < to_ascii < 123:
    print('lowercase')

# def char_to_num():
#     char = input()
#     to_ascii = ord(char)
#     if 64 < to_ascii < 91:
#         print('uppercase')
#     elif 96 < to_ascii < 123:
#         print('lowercase')

# char_to_num()

count = 1
while count <= 10:
    count += 1
print(count)

def sum_to_100():
  sum = 0
  num = 1

  while num<=100:
    sum += num
    num += 1

  return sum
 
print(sum_to_100())
 
