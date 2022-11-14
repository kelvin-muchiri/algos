"""
https://www.youtube.com/watch?v=YWbBFOsN7I0&ab_channel=praveen
https://www.youtube.com/watch?v=4rin1enhuQQ&ab_channel=TechandNavid
"""


def flippingMatrix(matrix):
    N = len(matrix)
    s = 0

    for i in range(N // 2):
        for j in range(N // 2):
            s += max(matrix[i][j], matrix[i][N-j-1],
                     matrix[N-i-1][j], matrix[N-i-1][N-j-1])

    return s


if __name__ == "__main__":
    print(flippingMatrix([[1, 2], [3, 4]]))
    print(flippingMatrix([[112, 42, 83, 119], [56, 125, 56, 49], [
          15, 78, 101, 43], [62, 98, 114, 108]]))
