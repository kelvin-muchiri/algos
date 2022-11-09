def solution(arr):
    if not arr:
        return 1

    greatest = arr[0]

    for i in range(len(arr)):
        num = arr[i]

        if num > greatest:
            greatest = num

    if greatest <= 0:
        return 1

    if greatest - 1 not in arr:
        return greatest - 1

    return greatest + 1


if __name__ == "__main__":
    print(solution([1, 3, 6, 4, 1, 2]))
    print(solution([1, 2, 3]))
    print(solution([-1, -3]))
