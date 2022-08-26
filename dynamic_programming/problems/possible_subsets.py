"""
Write a method to return all subsets of a set.
"""


def possible_subsets(arr, index):
    all_subsets = []

    if len(arr) == index:

        # Base case add empty set
        all_subsets.append([])

    else:
        all_subsets = possible_subsets(arr, index + 1)
        item = arr[index]
        more_subsets = []

        for subset in all_subsets:
            new_subset = []
            new_subset += subset
            new_subset.append(item)
            more_subsets.append(new_subset)

        all_subsets += more_subsets

    return all_subsets


if __name__ == "__main__":
    print(possible_subsets(['a', 'b'], 0))
