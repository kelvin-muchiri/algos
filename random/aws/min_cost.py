def min_cost_asc(alist):
    i = 0
    current_min_cost = 0

    while i < len(alist) - 1:
        if alist[i + 1] < alist[i]:
            # the next element violates asc
            # continously inc next element until
            # it just surpasses current element

            # reset current min cost
            current_min_cost = 0

            while alist[i + 1] < alist[i]:
                alist[i + 1] += 1
                current_min_cost += 1

        i += 1

    return current_min_cost


def min_cost_desc(alist):
    i = 0
    current_min_cost = 0

    while i < len(alist) - 1:
        if alist[i + 1] > alist[i]:
            # next element violates des, continously
            # decrement next element until it's just equal to current element

            # reset current min cost
            current_min_cost = 0

            while alist[i + 1] > alist[i]:
                alist[i + 1] -= 1
                current_min_cost += 1

        i += 1

    return current_min_cost


if __name__ == "__main__":
    print(min_cost_asc([0, 1, 2, 5, 6, 5, 7]))
    print(min_cost_desc([9, 8, 7, 2, 3, 3]))
