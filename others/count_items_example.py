# SANTIAGO GARCIA ARANGO
# PROBLEM TO SOLVE:
# Given a list of integers, return a dictionary with the structure:
# {"specific_integener": "amount_of_those_integers_in_list", ...}
# Example:
# Input [1, 2, 2, 3]
# Output {1: 1, 2: 2, 3: 1}

def perform_special_count(items_list):
    items_dict = {}
    for value in items_list:
        if value in items_dict:
            items_dict[value] = items_dict[value] + 1
        else:
            items_dict[value] = 1
    return(items_dict)


if __name__ == "__main__":
    # EXAMPLES
    print("----- EXAMPLE 1 -----")
    items_list = [1, 2, 2, 3]
    print(" Input: ", items_list)
    print(" Output: ", perform_special_count(items_list))

    print("----- EXAMPLE 2 -----")
    items_list = [3, 3, 3, 2, 2, 1]
    print(" Input: ", items_list)
    print(" Output: ", perform_special_count(items_list))

    print("----- EXAMPLE 3 -----")
    items_list = [1, 2, 3, 4, 5, 2, 4, 5, 3, 2, 1, 4, 2, 2, 2, 2, 3, 4]
    print(" Input: ", items_list)
    print(" Output: ", perform_special_count(items_list))
