#
# Complete the 'getFinalString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def getFinalString(s):
    # Write your code here
    while 'AWS' in s:
        splitted = s.split('AWS')
        s = ''.join(splitted)
    if len(s) == 0:
        return '-1'
    else:
        return s
    
print(getFinalString('AAWSWS'))
print(getFinalString('AWAWSSG'))
print(getFinalString('ABCDE'))

