"""Question

https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
"""


permutations = []


def num_permutations(i, perm, current_sum, s, d, m):
    if len(perm) == m:
        if current_sum == d:
            permutations.append(perm)
            return True

    if i == len(s):
        return False

    perm.append(s[i])
    new_index = i + 1
    new_sum = current_sum + s[i]

    if num_permutations(new_index, perm, new_sum, s, d, m):
        return True

    perm.pop()

    return False


def birthday(s, d, m):
    for i in range(len(s)):
        num_permutations(i, [], 0, s, d, m)


if __name__ == "__main__":
    birthday([2, 2, 1, 3, 2], 4, 2)
    print(permutations)
