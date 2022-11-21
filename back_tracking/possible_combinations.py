
"""
You are given a array of strings A of length N.

You have to return another string array which contains all possible special strings in Lexicographic order.
A special string is defined as a string with length equal to N,
and ith character of the string is equal to any character of the ith string in the array A.

https://www.interviewbit.com/problems/all-possible-combinations/
"""


def possible_combine(A):
    if not A:
        return ['']

    suffixes = possible_combine(A[1:])
    ans = [char + suff for char in A[0] for suff in suffixes]
    return ans


if __name__ == "__main__":
    print(possible_combine(['ab', 'cd']))
    print(possible_combine(["ozqz", "p", "abm"]))
