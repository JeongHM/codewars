# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.

# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


def sort_array(source_array):
    order = {n: i for n, i in enumerate(source_array) if i % 2 != 0}
    for l, v in zip(sorted(order.keys()), sorted(order.values())):
        source_array[l] = v
    return source_array


sort_array([5, 3, 2, 8, 1, 4])
