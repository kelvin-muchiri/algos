"""
Given a string s, return the longest palindromic substring in s.


Notes:
https://www.youtube.com/watch?v=UflHuQj6MVA
"""


def longest_palindrome(string):
    table = [[0 for j in range(len(string))] for i in range(len(string))]

    # every string of length 1 is a palindrome
    for i in range(len(string)):
        table[i][i] = 1

    longest_pal = string[0]

    # check for substring of length 2
    for i in range(len(string) - 1):
        # if start string and end string are equal, then it's a palindrome
        if string[i] == string[i + 1]:
            table[i][i+1] = 1

            if not len(longest_pal) == 2:
                longest_pal = string[i] * 2

    # check for lengths greater than 2
    current_length = 3

    while current_length <= len(string):
        i = 0

        while i < (len(string) - current_length + 1):
            j = i + current_length - 1

            if (table[i + 1][j - 1] and
                    string[i] == string[j]):
                table[i][j] = 1

                s = string[i:j + 1]

                if len(s) > len(longest_pal):
                    longest_pal = s

            i += 1

        current_length += 1

    return longest_pal


if __name__ == "__main__":
    print(longest_palindrome("babad"))
    print(longest_palindrome("cbbd"))
    print(longest_palindrome("a"))
    print(longest_palindrome("ac"))
