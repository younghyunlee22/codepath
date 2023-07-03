def expand_strings(strings):
  return ''.join(strings).upper() * 5

print(expand_strings(['x','y','z']))
print(expand_strings(['ab','cd','ef', 'gh']))

def upper_lower_count(str):
  num_upper = 0
  num_lower = 0

  for c in str:
    if not(c.isalpha()):
      continue

    if c == c.upper():
      num_upper += 1 
    else:
      num_lower += 1

  print('Num of uppercase:', num_upper)
  print('Num of lowercase:', num_lower)


def capitalization(str):
  #split by white space to a list
  #['sentence1', 'sentence2', 'sentence3']
  splitted = str.split('. ')
  for i in range(len(splitted)):
    splitted[i] = splitted[i].capitalize()
  result = '. '.join(splitted)
  return result

test_string = "speak from my heart. Speak from my soul. say what you want."
print(capitalization(test_string))

#teacher's code
def fix_capitalization(paragraph):
  sentences = paragraph.split('. ')

  for i, sentence in enumerate(sentences):
    sentences[i] = sentence.capitalize()

  return '. '.join(sentences)
  
print(fix_capitalization('speak from my heart. Speak from my soul. say what you want.'))
