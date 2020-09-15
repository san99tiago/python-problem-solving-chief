# SOL 1 PRAGMA
# Santiago Garcia Arango

# Complete the 'restock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY itemCount
#  2. INTEGER target
#

def restock(itemCount, target):
    itemCount.pop(0)
    total = 0
    for i in range(len(itemCount)):
        if target > total:
            total = total + itemCount[i]
        else:
            break

    return(abs(total-target))

if __name__ == '__main__':
    itemCount = [5, 1, 2, 3, 2, 1]
    target = 4
    print(restock(itemCount, target))

    itemCount = [4, 6, 1, 2, 1]
    target = 100
    print(restock(itemCount, target))

