"""
https://www.interviewbit.com/problems/letter-phone/
"""


class Solution:
    # @param A : string
    # @return a list of strings
    def letter_combination_util(self, parsed_string):
        if not parsed_string:
            return ['']

        suffixes = self.letter_combination_util(parsed_string[1:])
        ans = [ch + suffix for ch in parsed_string[0] for suffix in suffixes]
        return ans

    def letterCombinations(self, A):
        lookup = {
            '0': '0',
            '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        parsed_string = []

        for i in range(len(A)):
            parsed_string.append(lookup[A[i]])

        return self.letter_combination_util(parsed_string)


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations('23'))
