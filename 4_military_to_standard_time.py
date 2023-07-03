#
# Complete the 'military_to_standard' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER hours
#  2. INTEGER mins
#

def military_to_standard(hours, mins):
    # Write your code here
    # AM hour: 0 - 11
    if hours < 12:
        if hours == 0:
            hours = 12
        if mins == 0:
            mins = '00'
        return f'{hours}:{mins}AM'
           
    # PM hour: 12 - 23
    else:
        if hours != 12:
            hours = hours - 12
        if mins == 0:
            mins = '00'
        return f'{hours}:{mins}PM'