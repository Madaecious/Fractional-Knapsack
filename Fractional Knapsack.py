##############################################################################################
# Fractional Knapsack Problem Solved Using Greedy Approach
# Mark Barros - BID 013884117
# CS3310 - Design and Analysis of Algorithms
# Cal Poly Pomona: Spring 2021
##############################################################################################

# This is an import for reading csv files.
import csv

# This is the class that implements the fractional knapsack algorithm.
class Itemvalue:
    def __init__(self, weight, value, item):
        self.weight = weight
        self.value = value
        self.item = item
        self.cost = value // weight

    def __lt__(self, other):
        return self.cost < other.cost

# This is the magic part.
def solveKnapsack(weights, profits, items, capacity):

    # This declares the values and initializes them to null.
    items_list = []
    knapsack_value = 0
    knapsack_weights = []
    knapsack = []

    for i in range(len(weights)):
        items_list.append(Itemvalue(weights[i], profits[i], items[i]))

    # This sorts items by value.
    items_list.sort(reverse = True)

    # This handles the whole items first and then the partial item last.
    for item in items_list:

        if capacity - item.weight >= 0:
            capacity -= item.weight
            knapsack_value += item.value
            knapsack.append(item.item)
            knapsack_weights.append(item.weight)
        else:
            fraction = capacity / item.weight
            knapsack_value += item.value * fraction
            knapsack.append(item.item)
            knapsack_weights.append(round(fraction, 2))
            capacity -= int(item.weight * fraction)
            break

    return knapsack, knapsack_weights, round(knapsack_value, 2)

# This is the driver code. -------------------------------------------------------------------
if __name__ == "__main__":

    # This opens the input file as a csv.
    input_file = open('input.txt', 'r')
    reader = csv.reader(input_file)

    # These are the necessary variables.
    values = []
    knapsack_capacity = []
    item_types = []
    item_weights = []
    item_profits = []
    
    # This reads in the values.
    for row in reader:
        values.append(row)
    
    # This maps the values in the input file to the variables.
    knapsack_capacity = values[0]
    knapsack_capacity = list(map(int, knapsack_capacity))
    item_types = values[1]
    item_weights = values[2]
    item_weights = list(map(int, item_weights))
    item_profits = values[3]
    item_profits = list(map(int, item_profits))

    # This invokes the magic.
    knapsack_items, knapsack_weights, knapsack_value =  \
        solveKnapsack(\
                    item_weights, \
                    item_profits, \
                    item_types, \
                    knapsack_capacity[0] \
                    )

    # This it the console output.
    print("---------------------------------------------------------------------------")
    print("\tMark's Unbelievable Fractional Knapsack Results:\n")
    print("\tCapacity of the Knapsack: ", str(knapsack_capacity)[1:-1])
    print("\tItems in Knapsack: ", str(knapsack_items)[1:-1])
    print("\tCorresponding Weights of Items: ", str(knapsack_weights)[1:-1])
    print("\tMaximum Profit in Knapsack: ", knapsack_value)
    print("---------------------------------------------------------------------------")

# This is the end of the story. ##############################################################