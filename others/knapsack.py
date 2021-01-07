# Santiago Garcia Arango

# THIEF BAG PROBLEM (ZERO ONE KNAPSACK PROBLEM):
# https://en.wikipedia.org/wiki/Knapsack_problem

"""
The knapsack problem is a problem in combinatorial optimization: Given a set
of items, each with a weight and a value, determine the number of each item
to include in a collection so that the total weight is less than or equal to
a given limit and the total value is as large as possible.

It derives its name from the problem faced by someone who is constrained by
a fixed-size knapsack and must fill it with the most valuable items.

The name "knapsack problem" dates back to the early works of the mathematician
"Tobias Dantzig"(1884–1956).

--> Source: Wikipedia.
"""

def knapsack(bag_size, items_weight, items_value, n):
    # This is our "base-case-1" (no more items or bag is full)
    if n == 0 or bag_size == 0:
        return 0

    # This is our "base-case-2" (current item exceeds maximum bag_size)
    if items_weight[n - 1] > bag_size:
        return knapsack(bag_size, items_weight, items_value, n - 1)


    return max(items_value[n - 1] + knapsack(bag_size - items_weight[n - 1], items_weight, items_value, n - 1),
                knapsack(bag_size, items_weight, items_value, n - 1))




if __name__ == "__main__":
    # TEST 1
    items_value = [60, 100, 120]
    items_weight = [10, 20, 30]
    bag_size = 50
    n = len(items_value)
    best_result = knapsack(bag_size, items_weight, items_value, n)
    print("\nTEST 1 RESULT:", best_result)

    # TEST 2
    items_value = [60, 100, 120]
    items_weight = [10, 20, 30]
    bag_size = 60
    n = len(items_value)
    best_result = knapsack(bag_size, items_weight, items_value, n)
    print("\nTEST 2 RESULT:", best_result)

    # TEST 3
    items_value = [60, 100, 120]
    items_weight = [10, 20, 30]
    bag_size = 25
    n = len(items_value)
    best_result = knapsack(bag_size, items_weight, items_value, n)
    print("\nTEST 3 RESULT:", best_result)

    # TEST 4
    items_value = [60, 100, 120]
    items_weight = [10, 20, 30]
    bag_size = 30
    n = len(items_value)
    best_result = knapsack(bag_size, items_weight, items_value, n)
    print("\nTEST 4 RESULT:", best_result)

    # TEST 5
    items_value = [60, 100, 120]
    items_weight = [10, 20, 30]
    bag_size = 0
    n = len(items_value)
    best_result = knapsack(bag_size, items_weight, items_value, n)
    print("\nTEST 5 RESULT:", best_result)





