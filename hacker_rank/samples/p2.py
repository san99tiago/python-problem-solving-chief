# HACKER RANK SAMPLE PROBLEM
# Santiago Garcia Arango

# Complete the 'oddNumbers' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r

# Function recieves lower and upper limites (including them).
# we must return a list of odd numbers that are inbetween the limits.

import random

def oddNumbers(l, r):
    result = []
    for i in range(l, r+1):
        if i % 2 != 0:
            result.append(i)

    return(result)

if __name__ == "__main__":
    min_input = random.randint(1, 10)
    max_input = random.randint(10, 20)

    print("MIN = ", min_input)
    print("MAX = ", max_input)

    print(oddNumbers(min_input, max_input))
