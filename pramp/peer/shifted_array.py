"""
https://www.pramp.com/challenge/N5LYMbYzyOtbpovQoYPX
"""


def binary_search(arr, start, end, num):
    while start <= end:
        mid = start + (end - start) // 2

        if (arr[mid] < num):
            start = mid + 1
        elif (arr[mid] == num):
            return mid
        else:
            end = mid - 1

    return -1


def find_pivot(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if mid == 0 or arr[mid] < arr[mid-1]:
            return mid

        if arr[mid] > arr[0]:
            start = mid + 1
        else:
            end = mid - 1

    return 0


def shifted_arr_search(shiftArr, num):
    pivot = find_pivot(shiftArr)

    if pivot == 0 or num < shiftArr[0]:
        return binary_search(shiftArr, pivot, len(shiftArr) - 1, num)

    return binary_search(shiftArr, 0, pivot - 1, num)


if __name__ == "__main__":
    print(shifted_arr_search([2], 2))
    print(shifted_arr_search([9, 12, 17, 2, 4, 5], 2))
