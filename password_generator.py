import random
import string

length = int(input("Enter a number: "))

def random_password(length):
  password = ''
  for i in range(length):
    char_type = random.choice(['letter', 'num', 'schar'])
    if char_type == 'letter':
      password += random.choice(string.ascii_letters)
    elif char_type == 'num':
      password += random.choice(string.digits)
    else:
      password += random.choice(string.punctuation)

  return password

print('Your password is', random_password(length))