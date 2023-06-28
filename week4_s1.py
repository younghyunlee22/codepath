# count vowels

word = input('Enter a word: ')

num_vowels = 0

for c in word:
  if c in 'aeiouAEIOU':
    num_vowels += 1

print('Number of vowels:', num_vowels)

# split a bill
bill_amount = input('How much is the bill? ')
party_size = input('How many people are in your party? ')

if '$' == bill_amount[0]:
  bill_amount = bill_amount[1:]

split_bill = float(bill_amount) / int(party_size)

print('Each person owes $' + str(round(split_bill, 2)))

# sum and average of digits in a string
def sum_and_average(s):
    sum = 0
    digit_count = 0
    for i in range(len(s)):
      if 47 < ord(s[i]) < 58 : #s[i].isnumeric()
        sum += int(s[i])
        digit_count += 1
    average_is = sum/digit_count
    print(f'Sum of digits: {sum} \n Average of digists: {average_is}')

sum_and_average('of0923j2fn20fn2vn8239rjr4324k230')


def digits_in_string(s):
  total = 0
  num_digits = 0

  max_substr_len = 0
  curr_substr_len = 0

  for c in s:
    if c in '0123456789': # c.isnumeric()
      total += int(c)
      num_digits += 1

      curr_substr_len += 1
    else:
      curr_substr_len = 0

    if curr_substr_len > max_substr_len:
      max_substr_len = curr_substr_len
  
  print('The sum is:', total)
  print('The average is:', total/num_digits)
  print('The longest consecutive substring of numeric characters are:', max_substr_len)

digits_in_string('of0923j2fn20fn2vn8239rjr4324k230')
digits_in_string('123456abcdef')

