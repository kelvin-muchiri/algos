"""Write a program to print all permutations of a given string

References:
https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
https://www.youtube.com/watch?v=GuTPwotSdYw&ab_channel=takeUforward
https://www.youtube.com/watch?v=YK78FU5Ffjw&ab_channel=takeUforward

Time complexity:
O(n*n!) Note that there are n! permutations and it requires O(n) time to print a permutation.

Auxiliary space: O(r - l)
"""


class Solution1:
    """Uses backtracking"""

    def toString(self, List):
        return ''.join(List)

    # Function to print permutations of string
    # This function takes three parameters:
    # 1. String
    # 2. Starting index of the string
    # 3. Ending index of the string.

    def permute(self, a, l, r):
        if l == r:
            print(self.toString(a))
        else:
            for i in range(l, r):
                a[l], a[i] = a[i], a[l]
                self.permute(a, l+1, r)
                a[l], a[i] = a[i], a[l]  # backtrack


class Solution2:
    """Uses array"""

    def permute(self, string):
        ans = []
        ds = []
        freq = [False for i in range(len(string))]
        self.recur_permute(list(string), ds, ans, freq)
        return ans

    def recur_permute(self, string, ds, ans, freq):
        if len(ds) == len(string):
            ans.append("".join(ds))
            return

        for i in range(len(string)):
            if not freq[i]:
                freq[i] = True
                ds.append(string[i])
                self.recur_permute(string, ds, ans, freq)
                ds.pop()
                freq[i] = False


# Driver program to test the above function
if __name__ == "__main__":
    string = "ABC"
    n = len(string)
    a = list(string)

    sol1 = Solution1()
    sol1.permute(a, 0, n)

    sol2 = Solution2()
    print(sol2.permute(a))
