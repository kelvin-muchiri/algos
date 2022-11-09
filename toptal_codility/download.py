import math


def download(X, B, Z):
    if X == 0:
        return -1

    bytes_downloaded = 0

    for i in range(len(B)):
        bytes_downloaded += B[i]

    if bytes_downloaded == X:
        # file completely downloaded
        return 0

    bytes_rem = X - bytes_downloaded
    z_avg = 1

    if Z > len(B):
        # fewer than Z observations, we use Z
        z_avg = Z

    else:
        # if Z = 1 and 1 we have 1 observation
        if Z == 1 and len(B) == 1:
            z_avg = B[0]

        else:
            # get the average of the last Z observations
            i = len(B) - 1
            observation_sum = 0
            z_obervations_added = 0

            while i >= 0 and z_obervations_added < Z:
                observation_sum += B[i]
                z_obervations_added += 1
                i -= 1

            z_avg = observation_sum / Z

    time_rem = bytes_rem / z_avg

    return math.ceil(time_rem)


if __name__ == "__main__":
    print(download(100, [10, 6, 6, 8], 2))
    print(download(10, [2, 3], 2))
    print(download(10, [2], 1))
