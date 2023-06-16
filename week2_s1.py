import random
import string

def random_pass_gen(): 
    random_password = ''
    
    for i in range(4):
        random_letter = random.choice(string.ascii_letters)
        random_password += random_letter
        #random_password = random_password + random_letter
        
    for i in range(4):
        random_num = random.randint(0, 9)
        random_password += str(random_num)
    
    print(random_password)

# str(random.randint(1000, 9999))
# .join(random.choices(string.ascii_letters, k = letterLegnth))

# without a loop
def generate_password():
  random_password = ''

  # Genreate 4 random letters and add it to the random_password string
  random_password += random.choice(string.ascii_letters)
  random_password += random.choice(string.ascii_letters)
  random_password += random.choice(string.ascii_letters)
  random_password += random.choice(string.ascii_letters)
  
  # Generate 4 random digits and add it to the random_password string
  random_password += str(random.randint(0, 9))
  random_password += str(random.randint(0, 9))
  random_password += str(random.randint(0, 9))
  random_password += str(random.randint(0, 9))
  
  return random_password

print('Your new password is:', generate_password())

#----
def guess_number(guess):
  secret_number = random.randint(1, 100)
  print("psst: the secret number was", secret_number)
  
  if (guess < secret_number):
    return "secret number is higher"
  elif (guess > secret_number):
    return "secret number is lower"
  else:
    return "your guess was correct"

guess = int(input("Guess what the secret number is: "))
print(guess_number(guess))
