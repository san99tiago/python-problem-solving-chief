# HACKER RANK SAMPLE PROBLEM
# Santiago Garcia Arango

# Complete the 'findNumber' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k

# findNumber function returns if a number exists inside a list.
# If it does, return strin "YES", otherwise, return string "NO"

import random


def findNumber(arr, k):
    try:
        _ = arr.index(k)
        return "YES"
    except:
        return "NO"


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random.randint(1,20))

    k = random.randint(1,20)
    print("\narray = ", array)
    print("\nk = ", k)
    print(findNumber(array,k))
